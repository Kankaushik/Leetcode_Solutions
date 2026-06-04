/**
 * @return {Function}
 */
var createHelloWorld = function() {
    
    return function(...args) {
        args = "Hello World"
       return args
    }

};

const f = createHelloWorld();
f();

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */