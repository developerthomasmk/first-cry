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

        var eqpEl = `<div class="col-md-12">
        <div class="card shadow-0 border rounded-3">
          <div class="card-body">
            <div class="row g-0">
              <div class="col-xl-3 col-md-4 d-flex justify-content-center">
                <div class="bg-image hover-zoom ripple rounded ripple-surface me-md-3 mb-3 mb-md-0">
                  <img src="${productUrl}" class="w-100" />
                  
                </div>
              </div>
              <div class="col-xl-6 col-md-5 col-sm-7">
                <h5>${data.productname}</h5>
                <p class="text-muted">Category: Toys</p>
                <p class="text-muted">Posted by: User123</p>
                <br><br>

                <p class="text mb-4 mb-md-0">
                  ${data.desc} 
                </p>
              </div>
              <div class="col-xl-3 col-md-3 col-sm-5">
                <br><br><br><br>
                <div class="mt-4 d-flex align-items-center">
                  <input type="text" class="form-control input-box" placeholder="${data.price}">
                  <button class="btn btn-primary shadow-1 ml-2" type="button">SUBMIT</button>
                </div>
                <form class="dropdown">
                  <!-- <label for="status">Select an Option</label> -->
                  <select id="status" name="status">
                    <option value="Select one">Select One</option>
                    <option value="Accept">Accept</option>
                    <option value="Reject">Reject</option>
                  </select>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>`;

        adminContainer.innerHTML += eqpEl;
    });
}
