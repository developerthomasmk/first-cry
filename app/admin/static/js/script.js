document.addEventListener('DOMContentLoaded', () => {
  fetchUserData();
});

async function fetchUserData() {
  try {
    const response = await fetch(getDataUrl);
    const data = await response.json();
    console.log(data)
    if (data.status != 'failed') {
      loadData(data)
    }
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

function loadData(dataJson) {
  var adminContainer = document.getElementById("admin_container");
  adminContainer.innerHTML = "";

  console.log(dataJson.data)

  dataJson.data.forEach((data, index) => {

    const productUrl = `${productImageUrl}/${data.image}`

    // var eqpEl = `<div class="col-md-12">
    //     <div class="card shadow-0 border rounded-3">
    //       <div class="card-body">
    //         <div class="row g-0">
    //           <div class="col-xl-3 col-md-4 d-flex justify-content-center">
    //             <div class="bg-image hover-zoom ripple rounded ripple-surface me-md-3 mb-3 mb-md-0">
    //               <img src="${productUrl}" class="w-100" />

    //             </div>
    //           </div>
    //           <div class="col-xl-6 col-md-5 col-sm-7">
    //             <h5>${data.productname}</h5>
    //             <p class="text-muted">Category: Toys</p>
    //             <p class="text-muted">Posted by: User123</p>
    //             <br><br>

    //             <p class="text mb-4 mb-md-0">
    //               ${data.desc} 
    //             </p>
    //           </div>
    //           <div class="col-xl-3 col-md-3 col-sm-5">
    //             <br><br><br><br>
    //             <div class="mt-4 d-flex align-items-center">
    //               <input type="text" class="form-control input-box" placeholder="${data.price}">
    //               <button class="btn btn-primary shadow-1 ml-2" type="button">SUBMIT</button>
    //             </div>
    //             <form class="dropdown">
    //               <!-- <label for="status">Select an Option</label> -->
    //               <select id="status${index}" name="status">
    //                 <option value="Select one">Select One</option>
    //                 <option value="Accept">Accept</option>
    //                 <option value="Reject">Reject</option>
    //               </select>
    //             </form>
    //           </div>
    //         </div>
    //       </div>
    //     </div>
    //   </div>`;

    // adminContainer.innerHTML += eqpEl;

    // Create card container
    const cardContainer = document.createElement('div');
    cardContainer.className = 'col-md-12';

    // Create card
    const card = document.createElement('div');
    card.className = 'card shadow-0 border rounded-3';

    // Create card body
    const cardBody = document.createElement('div');
    cardBody.className = 'card-body';

    // Create row
    const row = document.createElement('div');
    row.className = 'row g-0';

    // Left column with image
    const leftCol = document.createElement('div');
    leftCol.className = 'col-xl-3 col-md-4 d-flex justify-content-center';

    const imageContainer = document.createElement('div');
    imageContainer.className = 'bg-image hover-zoom ripple rounded ripple-surface me-md-3 mb-3 mb-md-0';

    const img = document.createElement('img');
    img.src = productUrl; // Replace with actual product URL
    img.className = 'w-100';

    imageContainer.appendChild(img);
    leftCol.appendChild(imageContainer);

    // Middle column with product details
    const middleCol = document.createElement('div');
    middleCol.className = 'col-xl-6 col-md-5 col-sm-7';

    const productName = document.createElement('h5');
    productName.textContent = data.productname; // Replace with actual product name

    const category = document.createElement('p');
    category.className = 'text-muted';
    category.textContent = 'Category: Toys';

    const postedBy = document.createElement('p');
    postedBy.className = 'text-muted';
    postedBy.textContent = 'Posted by: User123';

    const description = document.createElement('p');
    description.className = 'text mb-4 mb-md-0';
    description.textContent = data.desc; // Replace with actual description

    middleCol.appendChild(productName);
    middleCol.appendChild(category);
    middleCol.appendChild(postedBy);
    middleCol.appendChild(document.createElement('br'));
    middleCol.appendChild(document.createElement('br'));
    middleCol.appendChild(description);

    // Right column with input and button
    const rightCol = document.createElement('div');
    rightCol.className = 'col-xl-3 col-md-3 col-sm-5';

    const inputContainer = document.createElement('div');
    inputContainer.className = 'mt-4 d-flex align-items-center';

    const inputBox = document.createElement('input');
    inputBox.type = 'text';
    inputBox.className = 'form-control input-box';
    inputBox.id = 'price';
    inputBox.value = data.price; // Replace with actual price

    const submitButton = document.createElement('button');
    submitButton.className = 'btn btn-primary shadow-1 ml-2';
    submitButton.type = 'button';
    submitButton.textContent = 'SUBMIT';

    submitButton.onclick = function () {
      var dropdown = document.getElementById('dropdown');
      var selectedText = dropdown.value;
      var price = document.getElementById('price').value;
      console.log('Price' + selectedText)
      handleButtonClick(selectedText, price, data);
    };

    inputContainer.appendChild(inputBox);
    inputContainer.appendChild(submitButton);

    // Dropdown form
    const dropdownSelect = document.createElement("select");
    dropdownSelect.className = 'dropdown'
    dropdownSelect.setAttribute("id", "dropdown");

    // Array of options
    const options = [
      { value: "Select", text: "Select Option" },
      { value: "Accept", text: "Accept" },
      { value: "Reject", text: "Reject" }
    ];

    // Loop through the options array to create option elements
    options.forEach(optionData => {
      const option = document.createElement("option");
      option.setAttribute("value", optionData.value);
      option.textContent = optionData.text;
      dropdownSelect.appendChild(option);
    });

    rightCol.appendChild(document.createElement('br'));
    rightCol.appendChild(document.createElement('br'));
    rightCol.appendChild(document.createElement('br'));
    rightCol.appendChild(document.createElement('br'));
    rightCol.appendChild(inputContainer);
    rightCol.appendChild(dropdownSelect);

    // Append all columns to the row
    row.appendChild(leftCol);
    row.appendChild(middleCol);
    row.appendChild(rightCol);

    // Append row to card body
    cardBody.appendChild(row);

    // Append card body to card
    card.appendChild(cardBody);

    // Append card to card container
    cardContainer.appendChild(card);

    // Assuming you have a container in your HTML to append this card to
    adminContainer.appendChild(cardContainer); // Replace 'yourContainerId' with the actual container ID

  });
}

async function handleButtonClick(selectedText, price, data) {
  try {
    var accept_url = updateStatuAcceptUrl.replace('0', data.productId).replace('PlaceHolder1', 'active').replace('0', parseInt(price))
    var reject_url = updateStatuAcceptUrl.replace('0', data.productId).replace('PlaceHolder1', 'reject')
    if (selectedText == "Accept") {

      const response = await fetch(accept_url);
      const data = await response.json();
      console.log(data)
      if (data.status != 'failed') {
        if (confirm('Do you want to refresh the page?')) {
          location.reload();
        } else {
          console.log('User pressed Cancel.');
        }
      }

    } else if (selectedText == "Reject") {

      const response = await fetch(reject_url);
      const data = await response.json();
      console.log(data)
      if (data.status != 'failed') {
        alert('Success')
      }

    } else {
      alert("Please accept or reject the product!")
    }

  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

