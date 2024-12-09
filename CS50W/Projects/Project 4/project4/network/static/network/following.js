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
    const posts_list = document.getElementById("friends-posts-list");

  fetch(`/following?start=${start}&end=${end}`)
    .then((response) => response.json())
    .then((posts) => {
        if (posts.posts.length > 0) {
            let post;
            for (post of posts.posts) {
                let li = document.createElement("li")
                li.setAttribute("class", "new_post")
                
                post_date = new Date(post.post_timestamp)
                post_date = post_date.toUTCString()

                // Like button
                like_pressed = false;
                if (like_pressed === true) {
                    like_btn_emoji = "❤️"
                } else {
                    like_btn_emoji = "🤍"
                }

                // Edit button
                let is_viewer_owner = post.viewer_owner
                let edit_button =  is_viewer_owner ? `<button class="btn btn-primary" id="edit-button">Edit</button>` : ""

                li.innerHTML = `
                    <a href="profile/${post.post_owner}"><h4>${post.post_owner}</h4></a>
                    <p>${post.post_text}</p>
                    <p style="color: lightgray">${post_date}</p>
                    <div><span id="like_btn">${like_btn_emoji}</span> <span>${post.post_likes}</span></div>
                    ${edit_button}
                    <div id="comments">Comments to be implemented</div>
                `
                posts_list.append(li)
            }
        }
        else {
            let li = document.createElement("li")
            li.innerHTML = "No posts yet..."
            posts_list.appendChild(li)
        }
    });
}
