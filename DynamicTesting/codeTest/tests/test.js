var request = require('supertest');

var app = require('../app').app;

describe('Calculator unit tests', function(){
    it("happy case add", function(done){
        request(app)
            .get("/calculator/add?first=1.2&second=3.4")
            .set('Accept', 'application/json')
            .expect('Content-Type', /json/)
            .expect(200, {result : 4.6})
            .end(function (err) {
                if(err) {
                    return done(err);
                }
                return done();
            })
    });

    it("Sub Test Case", function(done){
        request(app)
            .get("/calculator/sub?first=1.2&second=3.4")
            .set('Accept', 'application/json')
            .expect('Content-Type', /json/)
            .expect(200, {result :(1.2 - 3.4)})
            .end(function (err) {
                if(err) {
                    return done(err);
                }
                return done();
            })
    });

    it("Multiply Test Case", function(done){
        request(app)
            .get("/calculator/mul?first=1.2&second=3.4")
            .set('Accept', 'application/json')
            .expect('Content-Type', /json/)
            .expect(200, {result : (1.2 * 3.4)})
            .end(function (err) {
                if(err) {
                    return done(err);
                }
                return done();
            })
    });

    it("Divide Test Case", function(done){
        request(app)
            .get("/calculator/div?first=1.2&second=3.4")
            .set('Accept', 'application/json')
            .expect('Content-Type', /json/)
            .expect(200, {result : (1.2 / 3.4)})
            .end(function (err) {
                if(err) {
                    return done(err);
                }
                return done();
            })
    });

    it("Missing Parameter 'first'", function (done) {
        request(app)
            .get("/calculator/add?second=3.4")
            .expect('Content-Type', /text/)
            .expect(400, "Missing required parameter 'first'")
            .end(function (err) {
                if(err) {
                    return done(err);
                }
                return done();
            })
    });

    it("Missing Parameter 'second'", function (done) {
        request(app)
            .get("/calculator/add?first=1.2")
            .expect('Content-Type', /text/)
            .expect(400, "Missing required parameter 'second'")
            .end(function (err) {
                if(err) {
                    return done(err);
                }
                return done();
            })
    });

    it("Wrong Parameter 'first'", function (done) {
        request(app)
            .get("/calculator/add?first=hello&second=3.4")
            .expect('Content-Type', /text/)
            .expect(400, "The parameter 'first' is not a number")
            .end(function (err) {
                if(err) {
                    return done(err);
                }
                return done();
            })
    });

    it("Wrong Parameter 'second'", function (done) {
        request(app)
            .get("/calculator/add?first=1.2&second=world")
            .expect('Content-Type', /text/)
            .expect(400, "The parameter 'second' is not a number")
            .end(function (err) {
                if(err) {
                    return done(err);
                }
                return done();
            })
    });

    it("Dividing by Zero'", function (done) {
        request(app)
            .get("/calculator/div?first=1.2&second=0")
            .expect('Content-Type', /text/)
            .expect(400, "Dividing by zero is not allowed")
            .end(function (err) {
                if(err) {
                    return done(err);
                }
                return done();
            })
    });
});
