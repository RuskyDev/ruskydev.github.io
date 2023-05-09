var Stor = (function () {
  var isSupported = function () {
    try {
      var storage = window.localStorage;
      var testKey = "__storjs_test__";
      storage.setItem(testKey, testKey);
      storage.removeItem(testKey);
      return true;
    } catch (e) {
      return false;
    }
  };

  var set = function (key, value, options) {
    var storage = window.localStorage;
    var data = { value: value };
    if (options && options.expires) {
      var date = new Date();
      date.setTime(date.getTime() + options.expires * 1000);
      data.expires = date.getTime();
    }
    storage.setItem(key, JSON.stringify(data));
  };

  var get = function (key, defaultValue) {
    var storage = window.localStorage;
    var data = storage.getItem(key);
    if (!data) {
      return defaultValue;
    }
    try {
      data = JSON.parse(data);
    } catch (e) {
      return defaultValue;
    }
    if (data.expires && data.expires < new Date().getTime()) {
      storage.removeItem(key);
      return defaultValue;
    }
    return data.value;
  };

  var remove = function (key) {
    var storage = window.localStorage;
    storage.removeItem(key);
  };

  return {
    isSupported: isSupported,
    set: set,
    get: get,
    remove: remove,
  };
})();
