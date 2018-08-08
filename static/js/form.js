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