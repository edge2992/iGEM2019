//
// Javascriptで細線化 NWG Algorithm
//      http://www.hundredsoft.jp/win7blog/log/eid119.html
//
this.nwg_method = function (g, w, h, x1, y1, x2, y2) {
  width = w;
  height = h;

  grid = new Buffer(width * height);
  for (var i = 0; i < g.length; i++) {
    grid[i] = ~g[i];
    g[i] = ~g[i];
  }

  var bFlag = true;

  for (var k = 0; k < 100 && bFlag; k++) {
    bFlag = false;
    for (var i = 0; i < g.length; i++) {
      g[i] = grid[i];
    }
    for (var y = y1; y < y2; y++) {
      for (var x = x1; x < x2; x++) {
        var i = y * w + x;
        if (g[i]) {
          // [p7 p0 p1]
          // [p6    p2]
          // [p5 p4 p3]
          var p0 = (g[i - w]) ? 1 : 0;
          var p1 = (g[i - w + 1]) ? 1 : 0;
          var p2 = (g[i + 1]) ? 1 : 0;
          var p3 = (g[i + w + 1]) ? 1 : 0;
          var p4 = (g[i + w]) ? 1 : 0;
          var p5 = (g[i + w - 1]) ? 1 : 0;
          var p6 = (g[i - 1]) ? 1 : 0;
          var p7 = (g[i - w - 1]) ? 1 : 0;
          var a = 0;
          if (!p0 && p1) { a++; }
          if (!p1 && p2) { a++; }
          if (!p2 && p3) { a++; }
          if (!p3 && p4) { a++; }
          if (!p4 && p5) { a++; }
          if (!p5 && p6) { a++; }
          if (!p6 && p7) { a++; }
          if (!p7 && p0) { a++; }
          var b = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7;

          if (2 <= b && b <= 6) {
            var c = 0;
            if ((p0 + p1 + p2 + p5 == 0 && p4 + p6 == 2)
              || (p2 + p3 + p4 + p7 == 0 && p0 + p6 == 2)) {
              c = 1;
            }
            if (a == 1 || c == 1) {
              var e = (p2 + p4) * p0 * p6;
              var f = (p0 + p6) * p2 * p4;
              if ((!(k & 1) && e == 0) || ((k & 1) && f == 0)) {
                grid[i] = 0;
                bFlag = true;
              }
            }
          }
        }
      }
    }
  }
  for (var i = 0; i < grid.length; i++) {
    g[i] = ~g[i];
    grid[i] = ~grid[i];
  }
};