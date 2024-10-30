import time
import threading
import functools
import pickle
import hashlib
from collections import OrderedDict


def make_cache_key(args, kwargs):
    try:
        key = (args, frozenset(kwargs.items()))
        hash(key)
        return key
    except TypeError:
        key_data = (args, kwargs)
        key_bytes = pickle.dumps(key_data)
        key_hash = hashlib.md5(key_bytes).hexdigest()
        return key_hash


def conditional_cache(expiry, condition, max_size=5):
    def decorator(func):
        cache = OrderedDict()
        cache_lock = threading.Lock()
        computation_events = {}

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not condition(*args, **kwargs):
                return None

            key = make_cache_key(args, kwargs)
            current_time = time.time()

            with cache_lock:
                keys_to_delete = []
                for k in list(cache.keys()):
                    res, timestamp = cache[k]
                    if current_time - timestamp >= expiry:
                        keys_to_delete.append(k)
                for k in keys_to_delete:
                    del cache[k]
                    if k in computation_events:
                        del computation_events[k]

                if key in cache:
                    result, _ = cache.pop(key)
                    cache[key] = (result, current_time)
                    return result

                if key in computation_events:
                    event = computation_events[key]
                    need_wait = True
                else:
                    event = threading.Event()
                    computation_events[key] = event
                    need_wait = False

            if need_wait:
                event.wait()
                with cache_lock:
                    if key in cache:
                        result, _ = cache.pop(key)
                        cache[key] = (result, current_time)
                        return result
                    else:
                        return None
            else:
                result = func(*args, **kwargs)

                with cache_lock:
                    cache[key] = (result, current_time)
                    while len(cache) > max_size:
                        old_key, _ = cache.popitem(last=False)
                        if old_key in computation_events:
                            computation_events[old_key].set()
                            del computation_events[old_key]
                    event.set()
                    del computation_events[key]

                return result

        return wrapper

    return decorator
