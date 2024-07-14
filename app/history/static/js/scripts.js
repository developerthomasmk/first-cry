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
        // if(data.msg == 'user not found'){
        //     window.location.href = getLoginUrl;
        // }
        // displayUserData(data);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

function loadData(dataJson) {
    var historyContainer = document.getElementById("history_container");
    historyContainer.innerHTML = "";

    console.log(dataJson.data)

    dataJson.data.forEach((data, index) => {
        // var eqpEl = `<div class="row">
        //         <img src="${data.images.displayImageUrl}" style="height: 263px; width: 350px;">
        //         <div class="description">
        //             <h5>${data.name}</h5>
        //         </div>
        //         <div class="details">
        //             <a href="../product_info/productInfo.html?id=${index + 1}"><i class="fa-solid fa-circle-info"></i></a>
        //         </div>
        //     </div>`;

        const productUrl = `${ productImageUrl }/${data.image}`

        var eqpEl = `<div class="product-detail">
                    <div class="product-images">
                        <img src="${productUrl}" alt="Product Image" class="main-image">
                    </div>
                    <div class="product-info">
                        <h1>${data.productname}</h1>
                        <p class="price">&#8364;${data.price}</p>
                        <p class="order-status">Order status: ${data.status}</p>
                        <p class="description">${data.desc}</p>
                    </div>
                </div>`;
        historyContainer.innerHTML += eqpEl;
    });
}