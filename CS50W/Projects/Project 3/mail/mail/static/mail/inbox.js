document.addEventListener("DOMContentLoaded", function () {
  // Use buttons to toggle between views
  document
    .querySelector("#inbox")
    .addEventListener("click", () => load_mailbox("inbox"));
  document
    .querySelector("#sent")
    .addEventListener("click", () => load_mailbox("sent"));
  document
    .querySelector("#archived")
    .addEventListener("click", () => load_mailbox("archive"));
  document
    .querySelector("#trash_can")
    .addEventListener("click", () => load_mailbox("trash_can"));
  document.querySelector("#compose").addEventListener("click", compose_email);

  // By default, load the inbox
  load_mailbox("inbox");

  // Listen for email sending to the internal server
  document
    .querySelector("#compose-form")
    .addEventListener("submit", (event) => {
      // Prevent the form from reloading
      event.preventDefault();

      // Send emails to the server
      send_email();
    });
});

function compose_email() {
  // Show compose view and hide other views
  document.querySelector("#emails-view").style.display = "none";
  document.querySelector("#compose-view").style.display = "block";
  const single_email = document.querySelector("#email-display-view");
  if (single_email !== null) {
    single_email.style.display = "none";
    single_email.innerHTML = "";
    single_email.remove();
  }

  // Clear out composition fields
  clear_composition();
}

function clear_composition() {
  document.querySelector("#compose-recipients").value = "";
  document.querySelector("#compose-subject").value = "";
  document.querySelector("#compose-body").value = "";
}

function load_mailbox(mailbox) {
  // Show the mailbox and hide other views
  document.querySelector("#emails-view").style.display = "block";
  document.querySelector("#compose-view").style.display = "none";
  const single_email = document.querySelector("#email-display-view");
  if (single_email !== null) {
    single_email.style.display = "none";
    single_email.innerHTML = "";
    single_email.remove();
  }

  // Show the mailbox name
  document.querySelector("#emails-view").innerHTML = `<h3>${
    mailbox.charAt(0).toUpperCase() + mailbox.slice(1)
  }</h3>`;

  // Load emails based on the selected mailbox
  load_emails(mailbox);
}

function send_email() {
  // Retrieve the data from the form
  const recipients = document.querySelector("#compose-recipients").value;
  const email_subject = document.querySelector("#compose-subject").value;
  const email_body = document.querySelector("#compose-body").value;

  // Send data to the /emails route
  // Use fetch API to create a promise
  fetch("/emails", {
    method: "POST",
    // Data in json format
    body: JSON.stringify({
      recipients: recipients,
      subject: email_subject,
      body: email_body,
    }),
  })
    // For debugging
    // Retrieve sent data in json format
    .then((response) => response.json())
    .then((res) => {
      // Print the sent data
      console.log(res);
    });

  // Clear out composition fields
  clear_composition();
}

function load_emails(mailbox) {
  // Get all the emails in the database
  fetch(`/emails/${mailbox}`)
    .then((response) => response.json())
    .then((emails) => {
      // Print the emails in the console
      console.log(emails);

      // Create a new element for all the emails
      emails_section = document.createElement("div");
      emails_list = document.createElement("ul");
      document
        .querySelector("#emails-view")
        .appendChild(emails_section)
        .appendChild(emails_list);

      // Create elements for emails
      if (emails.length === 0) {
        // If there are no emails in the mailbox let user know
        emails_section.innerHTML = `<h3>No emails in the ${
          mailbox.charAt(0).toUpperCase() + mailbox.slice(1)
        } section!</h3>`;
      } else {
        emails.forEach((email) => {
          // If emails are unread
          if (email.read === false) {
            // Attach the classes of the email
            email_class = "email unread";
          } else {
            email_class = "email read";
          }
          // Attach the rest of the email
          emails_list.innerHTML += `
          <a>
            <li class="${email_class}" data-email-id="${email.id}">

              Sender: ${email.sender}${"&nbsp".repeat(10)}Subject: ${
            email.subject
          }
              <span>
              Sent on: ${email.timestamp}
              </span>
            <li>
          </a>
          `;

          // Load an email when clicking on it
          document
            .querySelector(".email")
            .addEventListener("click", (event) => {
              // Get the identifier for the email
              const database_email_id = event.target.dataset.emailId;

              // Check for trash email
              let is_disabled = "";
              let permanently_delete_email = "";
              if (mailbox === "trash_can") {
                is_disabled = "disabled";
                permanently_delete_email = `<button class="btn btn-sm btn-outline-danger left-side-button" id="permanently-delete" hidden>Delete Permanently</button>`;
              }

              // Create Archive Button
              let archive_button;
              if (email.archived === false) {
                archive_button = `<button class="btn btn-sm btn-outline-warning" id="archive-email-focused" ${is_disabled}>Archive</button>`;
              } else {
                archive_button = `<button class="btn btn-sm btn-outline-warning" id="archive-email-focused" ${is_disabled}>Unarchive</button>`;
              }

              // Create Delete Button
              let trash_button;
              if (email.is_trash === false) {
                trash_button = `<button class="btn btn-sm btn-outline-danger" id="trash">Move to Trash</button>`;
              } else {
                trash_button = `<button class="btn btn-sm btn-outline-danger" id="trash">Back to Inbox</button>`;
              }



              // Create a new view for the clicked email
              const element = document.createElement("div");
              element.setAttribute("id", "email-display-view");
              display_email_view(element);
              element.innerHTML = `

              <p><b>From: </b> ${email.sender}</p>
              <p><b>To: </b> ${email.recipients.join(", ")}</p>
              <p><b>Subject: </b> ${email.subject}</p>
              <p><b>Timestamp: </b> ${email.timestamp}</p>
              <button class="btn btn-sm btn-outline-primary" ${is_disabled} id="reply">Reply</button>
              ${archive_button}
              ${trash_button}
              ${permanently_delete_email}
              <hr>

              <p>${email.body}</p>
            `;

              // Mark email as read
              if (email.read === false) {
                fetch(`/emails/${email.id}`, {
                  method: "PUT",
                  body: JSON.stringify({
                    read: true,
                  }),
                });
              }

              // Archive email function
              const archived_button = document.querySelector(
                "#archive-email-focused"
              );
              archived_button.addEventListener("click", () => {
                if (email.archived === false) {
                  fetch(`/emails/${email.id}`, {
                    method: "PUT",
                    body: JSON.stringify({
                      archived: true,
                    }),
                  });
                  archived_button.innerHTML = "Unarchive";
                  location.reload();
                } else {
                  fetch(`/emails/${email.id}`, {
                    method: "PUT",
                    body: JSON.stringify({
                      archived: false,
                    }),
                  });
                  archived_button.innerHTML = "Archive";
                  location.reload();
                }
              });

              // Move to trash and back to inbox button
              const move_to_trash_button = document.querySelector("#trash");
              move_to_trash_button.addEventListener("click", () => {
                if (email.is_trash === false) {
                  fetch(`/emails/${email.id}`, {
                    method: "PUT",
                    body: JSON.stringify({
                      is_trash: true,
                    }),
                  });
                  move_to_trash_button.innerHTML = "Back to Inbox";
                  location.reload();
                } else {
                  fetch(`/emails/${email.id}`, {
                    method: "PUT",
                    body: JSON.stringify({
                      is_trash: false,
                    }),
                  });
                  archived_button.innerHTML = "Move to Trash";
                  location.reload();
                }
              });

              // Function to reply to emails
              let reply_btn = document.querySelector("#reply")
              reply_btn.addEventListener("click", () => {
                // Get elements to pre-populate the email fields
                let reply_send_to = email.sender;
                let reply_subject;
                let reply_body = `On ${email.timestamp} ${reply_send_to} wrote: ${email.body}`;
                if (email.subject.startsWith("Re: ")) {
                  reply_subject = email.subject.slice(4);
                } else {
                  reply_subject = `Re: ${email.subject}`;
                }
                
                // Pre-populate the compose area
                compose_email();
                document.querySelector("#compose-recipients").value = reply_send_to;
                document.querySelector("#compose-subject").value = reply_subject;
                document.querySelector("#compose-body").value = reply_body;
              })
            });
        });
      }

      //
    });
}

function display_email_view(element) {
  // Show displayed email view and hide other views
  document.querySelector("#emails-view").style.display = "none";
  document.querySelector("#compose-view").style.display = "none";
  document.querySelector(".container").appendChild(element);

  // Clear out composition fields
  clear_composition();
}
