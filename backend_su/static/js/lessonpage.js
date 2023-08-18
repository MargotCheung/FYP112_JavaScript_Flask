fetch('/api/comments') // 根據您的後端API設計，修改URL為適當的後端API路徑
  .then(response => response.json())
  .then(data => {
    const commentSection = document.getElementById('commentSection');
    commentSection.innerHTML = ''; // 清空留言板內容
    let commentCount = 0;

    data.forEach(comment => {
      commentCount++;
      

      const commentElement = document.createElement('div');
      commentElement.classList.add('comment');

      const authorElement = document.createElement('p');
      authorElement.classList.add('comment-author');
      authorElement.textContent = comment.author;

      const contentElement = document.createElement('p');
      contentElement.classList.add('comment-content');
      contentElement.textContent = comment.content;

      const footerElement = document.createElement('div');
      footerElement.classList.add('comment-footer');

      const floorElement = document.createElement('p');
      floorElement.classList.add('comment-floor');
      floorElement.textContent = `樓層: ${commentCount}`;//宛靜同學請增加這些變數在資料庫

      const likesElement = document.createElement('p');
      likesElement.classList.add('comment-likes');
      likesElement.textContent = `Like 人數: ${comment.likes}`;

      const replyButton = document.createElement('button');
      replyButton.classList.add('comment-reply-button');
      replyButton.textContent = '回覆';

      footerElement.appendChild(floorElement);
      footerElement.appendChild(likesElement);
      footerElement.appendChild(replyButton);

      commentElement.appendChild(authorElement);
      commentElement.appendChild(contentElement);
      commentElement.appendChild(footerElement);

      commentSection.appendChild(commentElement);
    });
  })
  .catch(error => {
    console.error('Error:', error);
  });


// 在文檔準備就緒時綁定事件處理程序
document.addEventListener('DOMContentLoaded', function() {
    // 獲取新增留言按鈕和子頁面模板
    const addCommentButton = document.querySelector('.add-comment-button');
    const addCommentTemplate = document.querySelector('#add-comment-template');
  
    // 監聽新增留言按鈕的點擊事件
    addCommentButton.addEventListener('click', function() {
      // 複製子頁面模板並插入到DOM中
      const addCommentModal = addCommentTemplate.innerHTML.cloneNode(true);
      console.log(addCommentModal);
      document.body.appendChild(addCommentModal);
  
      // 獲取子頁面中的元素
      const commentButton = document.querySelector('.comment-button');
      const cancelButton = document.querySelector('.cancel-button');
  
      // 監聽留言按鈕的點擊事件
      commentButton.addEventListener('click', function() {
        // 獲取留言暱稱
        const nicknameInput = document.querySelector('#nickname');
        const nickname = nicknameInput.value;
  
        // 在這裡執行留言提交的相關邏輯，例如發送請求保存留言
  
        // 關閉子頁面
        closeAddCommentModal();
      });
  
      // 監聽取消按鈕的點擊事件
      cancelButton.addEventListener('click', function() {
        // 關閉子頁面
        closeAddCommentModal();
      });
    });
  
    // 函數：關閉子頁面
    function closeAddCommentModal() {
      const addCommentModal = document.querySelector('.add-comment-modal');
      addCommentModal.remove();
    }
});
  