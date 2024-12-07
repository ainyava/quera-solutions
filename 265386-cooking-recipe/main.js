function prepare(gredients, callback) {
    return new Promise((r) => {
        console.log("preparing stuffs:", gredients.join(", "));
        setTimeout(() => {
            r(callback("preparing"));
        }, 500);
    });
}

function cooking(callback) {
    return new Promise((r) => {
        console.log("making an omelette ...");
        setTimeout(() => {
            r(callback("making"));
        }, 2000);
    });
}

function serve(callback) {
    return new Promise((r) => {
        console.log("serving food ...");
        setTimeout(() => {
            r(callback("serving"));
        }, 500);
    });
}

function eat(callback) {
    return new Promise((r) => {
        console.log("eating ...");
        setTimeout(() => {
            r(callback("eating"));
        }, 1000);
    });
}

function doneMessage(prevStep) {
    console.log(`${prevStep} done, next step ...`);
}

function startCooking(stuffs) {
    prepare(stuffs, doneMessage)
        .then(() => cooking(doneMessage))
        .then(() => serve(doneMessage))
        .then(() => eat(doneMessage))
        .then(() => console.log("process is done"));
}

// startCooking(["eggs", "tomatoes"]);

module.exports = { prepare, cooking, serve, eat, doneMessage };
