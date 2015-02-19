App = Ember.Application.create();

App.Router.map(function() {
 this.resource('TabOne');
 this.resource('TabTwo');
 this.resource('TabThree');
});


