this.zhang_suen = function (g, w, h, x1, y1, x2, y2) {
  width = w;
  height = h;

  grid = new Buffer(width * height);
  for (var i = 0; i < g.length; i++) {
    grid[i] = ~g[i];
    g[i] = ~g[i];
  }

  var bFlag = true;

  for (var k = 0; k < 100 && bFlag; k++) {
    if (!(k & 1)) {
      bFlag = false;
    }
    for (var i = 0; i < g.length; i++) {
      g[i] = grid[i];
    }
    for (var y = y1; y < y2; y++) {
      for (var x = x1; x < x2; x++) {
        var i = y * width + x;
        if (g[i]) {
          // [p9 p2 p3]
          // [p8 p1 p4]
          // [p7 p6 p5]
          var p1 = 1;
          var p2 = g[i - width] ? 1 : 0;
          var p3 = g[i - width + 1] ? 1 : 0;
          var p4 = g[i + 1] ? 1 : 0;
          var p5 = g[i + width + 1] ? 1 : 0;
          var p6 = g[i + width] ? 1 : 0;
          var p7 = g[i + width - 1] ? 1 : 0;
          var p8 = g[i - 1] ? 1 : 0;
          var p9 = g[i - width - 1] ? 1 : 0;

          var a = 0;
          if (!p2 && p3) { a++; }
          if (!p3 && p4) { a++; }
          if (!p4 && p5) { a++; }
          if (!p5 && p6) { a++; }
          if (!p6 && p7) { a++; }
          if (!p7 && p8) { a++; }
          if (!p8 && p9) { a++; }
          if (!p9 && p2) { a++; }
          var b = p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9;

          if (a == 1 && 2 <= b && b <= 6) {
            if ((!(k & 1) && p2 * p4 * p6 == 0 && p4 * p6 * p8 == 0) || ((k & 1) && p2 * p4 * p8 == 0 && p2 * p6 * p8 == 0)) {
              grid[i] = 0;
              bFlag = true;
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
