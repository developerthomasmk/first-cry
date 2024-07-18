document.addEventListener('DOMContentLoaded', () => {
  checkSession()
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
  var homeContainer = document.getElementById("home_container");
  homeContainer.innerHTML = "";

  console.log(dataJson.data)

  dataJson.data.forEach((data, index) => {

    const productUrl = `${productImageUrl}/${data.image}`

    var eqpEl = `<div class="col-sm-6 col-md-4 col-lg-3">
          <div class="box">
            <a href="">
              <div class="img-box">
                <img src="${productUrl}" alt="">
              </div>
              <div class="detail-box">
                <h6>
                  robot 
                </h6>
                <h6>
                  ${data.productname}
                  <span>
                    &#8364;${data.price}
                  </span>
                </h6>
              </div>
            </a>
          </div>
        </div>`;

    homeContainer.innerHTML += eqpEl;
  });
}

async function checkSession() {
  try {
    const response = await fetch(hasSessionUrl);
    const data = await response.json();
    var loginContainer = document.getElementById("login_container");
    loginContainer.innerHTML = "";

    console.log(response)

    if (data.has_data) {


      var eqpEl = `<a href="">
              <i class="fa fa-user" aria-hidden="true"></i>
              <span>
                Welcome ${data.username}
              </span>
            </a>
            <div>
            <a href="${getLogoutUrl}">
              <i class="fa fa-user" aria-hidden="true"></i>
              <span>
                logout
              </span>
            </a>
          </div>
          <div>
            <a href="${getDeleteUrl.replace('0', data.ueserid)}">
              <i class="fa fa-user" aria-hidden="true"></i>
              <span>
                delete account
              </span>
            </a>
          </div>`;



    } else {
      var eqpEl = `<a href=${getLoginUrl}>
              <i class="fa fa-user" aria-hidden="true"></i>
              <span>
                LOGIN
              </span>
            </a>`;
    }
    loginContainer.innerHTML += eqpEl;
  } catch (error) {
    console.error('Error checking session:', error);
  }
}