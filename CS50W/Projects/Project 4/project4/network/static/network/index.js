// When the index page has been fully loaded

// Start variables
let counter = 1; // The very last posted post
const quantity = 10; // How many posts we want to load at each scroll + initial load

document.addEventListener("DOMContentLoaded", () => {
  // Load the first content on page
  load();
});

window.onscroll = () => {
  if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
    load();
  }
};

function load() {
  // Set the start and end for db query and update counter for future requests
  const start = counter;
  const end = start + quantity - 1;
  counter = end + 1;

  // Get the latest posts from the database
  const posts_list = document.getElementById("posts-list");

  fetch(`/posts?start=${start}&end=${end}`)
    .then((response) => response.json())
    .then((posts) => {
      if (posts.posts.length > 0) {
        let post;
        for (post of posts.posts) {
          let li = document.createElement("li");
          li.setAttribute("class", "new_post");

          post_date = new Date(post.post_timestamp);
          post_date = post_date.toUTCString();

          let post_id = post.post_id

          // Like button
          like_pressed = false;
          if (like_pressed === true) {
            like_btn_emoji = "❤️";
          } else {
            like_btn_emoji = "🤍";
          }

          // Edit button
          let is_viewer_owner = post.viewer_owner;
          let e_button = document.createElement("button");
          e_button.setAttribute("class", "btn btn-primary");
          e_button.innerHTML = "Edit";
          let edit_button = is_viewer_owner ? e_button : null;

          li.innerHTML = `
                    <a href="profile/${post.post_owner}"><h4>${post.post_owner}</h4></a>
                    <p class="content">${post.post_text}</p>
                    <p style="color: lightgray">${post_date}</p>
                    <div><span id="like_btn">${like_btn_emoji}</span> <span>${post.post_likes}</span></div>
                    <div id="comments">Comments to be implemented</div>
                    `;

          if (edit_button !== null) {
            li.append(edit_button);
            edit_button.addEventListener("click", (event) => {
              text_element = event.target.parentElement.children[1];
              content = text_element.innerHTML;
              let textarea = document.createElement("textarea");
              textarea.setAttribute("class", "form-control");
              textarea.value = content;

              let curr_text = text_element;

              // Replace the Text with a Text area input
              text_element.parentNode.replaceChild(textarea, text_element);

              // Save the current element
              const curr_button = edit_button

              // Replace the Edit button with a submit button
              let submit = document.createElement("button");
              submit.innerHTML = "Save";
              submit.setAttribute("class", "btn btn-primary");
              event.target.replaceWith(submit)

              // Add the submit event
              submit.addEventListener("click", (event) => {
                // Send update data to the server
                console.log(post_id)
                fetch(`/edit/${post_id}`, {
                  method: "PUT",
                  body: JSON.stringify({
                    text: `${textarea.value}`
                  })
                })

                // Replace btn
                submit.replaceWith(curr_button);
                curr_text.innerHTML = textarea.value
                textarea.replaceWith(curr_text)
              })
            });
          }
          posts_list.append(li);
        }
      } else {
        let li = document.createElement("li");
        li.innerHTML = "No posts yet...";
        posts_list.appendChild(li);
      }
    });
}
