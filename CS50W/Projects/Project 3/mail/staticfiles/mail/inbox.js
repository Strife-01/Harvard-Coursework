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
  .querySelector("#compose")
  .addEventListener("click", compose_email);

  // By default, load the inbox
  load_mailbox("inbox");

  // Listen for email sending to the internal server
  document
  .querySelector("#compose-form")
  .addEventListener("submit", (event) => {

    // Prevent the form from reloading
    event.preventDefault();
    // event.preventImmediatePropagation();

    // Send emails to the server
    send_email();
  });
});

function compose_email() {
  // Show compose view and hide other views
  document.querySelector("#emails-view").style.display = "none";
  document.querySelector("#compose-view").style.display = "block";

  // Clear out composition fields
  document.querySelector("#compose-recipients").value = "";
  document.querySelector("#compose-subject").value = "";
  document.querySelector("#compose-body").value = "";
}

function load_mailbox(mailbox) {
  // Show the mailbox and hide other views
  document.querySelector("#emails-view").style.display = "block";
  document.querySelector("#compose-view").style.display = "none";

  // Show the mailbox name
  document.querySelector("#emails-view").innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)
    }</h3>`;

  // Load emails based on the selected mailbox
  // load_emails(mailbox);
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
}
