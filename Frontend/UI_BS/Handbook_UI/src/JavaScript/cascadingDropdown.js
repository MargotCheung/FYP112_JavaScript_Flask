var subjectObject = {
  "一上": {
    "必修": ["程式設計(I)", "程式設計(II)", "計算機概論", "微積分(一)"],
    "選修": [" "],
  },
  "一下": {
    "必修": ["程式設計(III)", "程式設計(IV)", "微積分(二)", "普通物理-電、磁、光實驗"],
    "選修": [" "],
  },
  "二上": {
    "必修": ["資料結構", "資料結構實習", "離散數學", "通訊與網路概論"],
    "選修": ["電子學", "電子學實驗", "物件導向設計", "物件導向設計實習"]
  },
  "二下": {
    "必修": ["系統程式", "機率與統計", "資料庫系統"],
    "選修": ["數位系統設計", "數位系統設計實驗", "系統分析與設計"]
  },
  "三上": {
    "必修": ["作業系統(一)", "微處理機系統", "微處理機系統實習"],
    "選修": ["編譯器", "軟體工程開發實務", "網路程式設計", "網路程式設計實習"],
  },
  "三下": {
    "必修": ["計算機結構學", "計算機演算法", "專題研究(一)"],
    "選修": ["人工智慧導論", "程式語言", "行動應用程式開發", "軟體框架設計"],
  },
  "四上": {
    "必修": ["專題研究(二)"],
    "選修": ["自然語言處理實務", "深度學習", "管理資訊系統", "無線網路系統"],
  },
  "四下": {
    "必修": [" "],
    "選修": ["智慧物聯網實務應用", "程式設計與問題解決"],
  }
}

window.onload = function() {
  var subjectSel = document.getElementById("subject");
  var topicSel = document.getElementById("topic");
  var chapterSel = document.getElementById("chapter");

  for (var x in subjectObject) {
    subjectSel.options[subjectSel.options.length] = new Option(x, x);
  }

  subjectSel.onchange = function() {
    // Empty Chapters- and Topics- dropdowns
    chapterSel.length = 1;
    topicSel.length = 1;

    // Display correct values
    for (var y in subjectObject[this.value]) {
      topicSel.options[topicSel.options.length] = new Option(y, y);
    }
  };

  topicSel.onchange = function() {
    // Empty Chapters dropdown
    chapterSel.length = 1;

    // Display correct values
    var z = subjectObject[subjectSel.value][this.value];
    for (var i = 0; i < z.length; i++) {
      chapterSel.options[chapterSel.options.length] = new Option(z[i], z[i]);
    }
  };
};
