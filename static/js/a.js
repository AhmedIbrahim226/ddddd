console.log('JS file connected!!!!!!');

const url = new URL(window.location.href)
const protocol = url.protocol
const port = url.port
const apiPathUrl = `${protocol}//www.localhost:${port}`


const waiting = document.querySelector('#waiting');

let appSelector = (selectObj) => {
    let val = selectObj.value
    if (val) {
        let spinnerTime = setTimeout(getProductTenant, 2000, val)
        $('#tenant-div-id').css('display', '');
    } else {
        waiting.innerHTML = `
        <div id="spinner" class="spinner-border" style="width: 2.4rem; height: 2.4rem;" role="status">
            Loading...
            <span class="visually-hidden">Loading...</span>
        </div>
        `
        $('#tenant-div-id').css('display', 'none');
    }
}

async function getProductTenant(tenantDomainId) {
    const response = await fetch(`${apiPathUrl}/api/tenant/retrieve/`, {
        method: 'POST',
        headers: {
            // 'X-CSRFTOKEN': "AllowAny",
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            'tenant_domain_id': tenantDomainId
        })
    })

    let data = response.json()

    let selectElement = document.createElement('select')


    data.then((result) => {
        let spinner = document.querySelector('#spinner');
        let option = document.createElement('option')
        option.value = ''
        option.text = '----------'
        selectElement.appendChild(option)
        
        result.forEach((item) => {
            let option = document.createElement('option')
            option.value = item['id']
            option.text = item['tenant_subdomain']
            selectElement.appendChild(option)
        })
        selectElement.classList.add('form-select')
        selectElement.setAttribute('name', 'tenant_id')
        selectElement.setAttribute('required', '')
        waiting.replaceChild(selectElement, spinner)

    }).catch((error) => {
        console.log(error);
    })
}


