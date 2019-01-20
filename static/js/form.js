let lastForm;

document.getElementById('formDropdown').onclick = function dropdownClick(event) {
    event.preventDefault();

    let item = event.target;

    let formType = item.getAttribute('data-form');

    let form = document.getElementById( formType + 'Form');
    form.className = form.className.replace('d-none','');

    if(lastForm) {
        lastForm.className += ' d-none';
    }

    lastForm = form;
};

function getFormData(evt) {

    if(evt) {
        evt.preventDefault(); //if evt is present then cancel the default event behaviour 
    }
    let data = {};
    let properties = [
        'name',
        'email',
        'subject',
        'message'
    ];
    let formId = 'contactForm';

    for(let i=0;i<properties.length;i++) {
        let prop = properties[i];
        data[prop] = document.getElementById(formId + '_' + prop).value;
    }

    console.log(data);
}
// sure about the below line? Yess, this is for the conatct form, not related to the application writer okay
document.getElementById('contactForm').onsubmit = getFormData;