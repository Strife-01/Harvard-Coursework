let counter = 1; // The very last posted post
const quantity = 10; // How many posts we want to load at each scroll + initial load
let username = window.location.href.split("/profile/")[1];

document.addEventListener("DOMContentLoaded", () => {
  // csrf token
  const csrfToken = document.querySelector("[name='csrf_token']").content;

  load_all_posts();

  // Check for need to follow
  const follow_btn = document.getElementById("follow");
  if (follow_btn != null) {
    follow_btn.addEventListener("click", () => {
      // Interact with the database
      fetch(`/follow_user/${username}`, {
        headers: {
          "X-CSRF-Token": csrfToken,
          "Content-Type": "application/json",
        },
        method: "PUT",
        credentials: "same-origin",
        body: JSON.stringify({
          action: "follow",
        }),
      }).then(() => window.location.reload());
    });
  }

  // Check for need to unfollow
  const unfollow_btn = document.getElementById("unfollow");
  if (unfollow_btn != null) {
    unfollow_btn.addEventListener("click", () => {
      // Interact with the database
      let username = window.location.href.split("/profile/")[1];
      fetch(`/follow_user/${username}`, {
        headers: {
          "X-CSRF-Token": csrfToken,
          "Content-Type": "application/json",
        },
        method: "PUT",
        credentials: "same-origin",
        body: JSON.stringify({
          action: "unfollow",
        }),
      }).then(() => window.location.reload());
    });
  }
});

function load_all_posts() {
  const posts_list = document.getElementById("user-posts-list");
  fetch(`/posts/${username}`)
    .then((response) => response.json())
    .then((posts) => {
      if (posts.posts.length > 0) {
        let post;
        viewer_username = posts.viewer_username;
        for (post of posts.posts) {
          let li = document.createElement("li");
          li.setAttribute("class", "new_post");

          post_date = new Date(post.post_timestamp);
          post_date = post_date.toUTCString();

          // Post text
          let post_text = post.post_text;

          // Post id
          let post_id = post.post_id;

          // Like button
          like_pressed = false;
          if (like_pressed === true) {
            like_btn_emoji = "❤️";
          } else {
            like_btn_emoji = "🤍";
          }

          li.innerHTML = `
                    <p>${post_text}</p>
                    <p style="color: lightgray">${post_date}</p>
                    <div><span id="like_btn">${like_btn_emoji}</span> <span>${post.post_like_count}</span></div>
                    <div id="comments">Comments to be implemented</div>
                `;

          // Edit
          if (viewer_username === username) {
            let e_button = document.createElement("button");
            e_button.setAttribute("class", "btn btn-primary");
            e_button.innerHTML = "Edit";
            e_button.addEventListener("click", (event) => {
              textarea = document.createElement("textarea");
              textarea.setAttribute("class", "form-control");
              textarea.value = post_text;
              text_element = event.target.parentElement.children[0];
              text_element.replaceWith(textarea);
              let submit = document.createElement("button");
              submit.setAttribute("class", "btn btn-primary");
              submit.innerHTML = "Save";
              e_button.replaceWith(submit);

              submit.addEventListener("click", (event) => {
                fetch(`/edit/${post_id}`, {
                  method: "PUT",
                  body: JSON.stringify({
                    text: `${textarea.value}`,
                  }),
                });

                text_element.innerHTML = textarea.value;
                textarea.replaceWith(text_element);
                submit.replaceWith(e_button);
              });
            });
            li.append(e_button);
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
