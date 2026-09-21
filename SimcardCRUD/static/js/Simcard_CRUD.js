document.addEventListener("DOMContentLoaded", function () {

CreateModalProcessing();
UpdateModalProcessing();
DeleteModalPreccessing();


});


function CreateModalProcessing() {
    // Getting Select-Option Widget of Tariff change for Create Modal
    const tariffSelect_crt =
        document.getElementById("ServiceType-create-name");

    // Tariff Info Icon Initialization on DOMContentLoaded (in Create Modal)
    const tariffInfoIcon_crt =
        document.getElementById("tariff-info-create-modal-icon");


    if (!tariffSelect_crt || !tariffInfoIcon_crt) {
        console.error("Tariff select or info icon not found");
        return;
    }
    
function getTariffInfo_crt() {

    const option =
        tariffSelect_crt.options[tariffSelect_crt.selectedIndex];

    if (!option) {
        return "Тариф не выбран";
    }

    return `
        <strong>${option.dataset.title}</strong><br>
        Минуты: ${option.dataset.minutes}<br>
        SMS: ${option.dataset.sms}<br>
        Гигабайты: ${option.dataset.gigabytes}<br>
        Стоимость: ${option.dataset.price} ₽
    `;
}


function createTariffPopover_crt() {

    return new bootstrap.Popover(
        tariffInfoIcon_crt,
        {
            html: true,
            trigger: "hover focus",
            // Container is important if popover is inside the modal
            container: "body",
            placement: "right",
            content: getTariffInfo_crt
        }
    );

}

// Creating Tariff Popover on DOMContentLoaded
let tariffPopover_crt = createTariffPopover_crt();


function refreshTariffPopover_crt() {

        tariffPopover_crt.dispose();

        tariffPopover_crt = createTariffPopover_crt();
}


tariffSelect_crt.addEventListener("change", function () {

    refreshTariffPopover_crt()


});



// Update Modal Window Initializing
const createModal =
    document.getElementById("createRecordModal");


let createModalTrigger = null;


function clearCreateForm() {

     document.getElementById("create-record-form").reset()

}


// Event that executes on create modal window show up
createModal.addEventListener(
    "show.bs.modal",
    function (event) {

        const button = event.relatedTarget;

        // For changing focus on modal close
        createModalTrigger = button;

        clearCreateForm()

        // Updating tariff info popover on create modal open after tariff is applied 
        refreshTariffPopover_crt()

    }
);


// Event on Create Modal Close
createModal.addEventListener(
    "hide.bs.modal",
    function () {

        if (createModal.contains(document.activeElement)) {
            document.activeElement.blur();
        }
    }
);


createModal.addEventListener(
    "hidden.bs.modal",
    function () {

        if (createModalTrigger) {
            createModalTrigger.focus();
        }
    }
);
    
}

function UpdateModalProcessing() {

// Getting Select-Option Widget of Tariff change for Create Modal
const tariffSelect_upd =
    document.getElementById("ServiceType-update-name");

// Tariff Info Icon Initialization on DOMContentLoaded (in Update Modal)
const tariffInfoIcon_upd =
    document.getElementById("tariff-info-update-modal-icon");


if (!tariffSelect_upd || !tariffInfoIcon_upd) {
    console.error("Tariff select or info icon not found in update modal");
    return;
}


// Ctrl + Shift + R --> Hard refresh 

function getTariffInfo_upd() {

    const option =
        tariffSelect_upd.options[tariffSelect_upd.selectedIndex];

    if (!option) {
        return "Тариф не выбран";
    }

    return `
        <strong>${option.dataset.title}</strong><br>
        Минуты: ${option.dataset.minutes}<br>
        SMS: ${option.dataset.sms}<br>
        Гигабайты: ${option.dataset.gigabytes}<br>
        Стоимость: ${option.dataset.price} ₽
    `;
}


function createTariffPopover_upd() {

    return new bootstrap.Popover(
        tariffInfoIcon_upd,
        {
            html: true,
            trigger: "hover focus",
            // Container is important if popover is inside the modal
            container: "body",
            placement: "right",
            content: getTariffInfo_upd
        }
    );

}

// Creating Tariff Popover on DOMContentLoaded
let tariffPopover_upd = createTariffPopover_upd();


function refreshTariffPopover_upd() {

        tariffPopover_upd.dispose();

        tariffPopover_upd = createTariffPopover_upd();
}


tariffSelect_upd.addEventListener("change", function () {

    refreshTariffPopover_upd()


});



// Update Modal Window Initializing
const updateModal =
    document.getElementById("updateRecordModal");


let updateModalTrigger = null;


// Event that executes on update modal window show up
updateModal.addEventListener(
    "show.bs.modal",
    function (event) {

        const button = event.relatedTarget;

        // For changing focus on modal close
        updateModalTrigger = button;

        const pk =
            button.dataset.pk;

        const imei =
            button.dataset.imei;

        const phone =
            button.dataset.phone;

        const clientName =
            button.dataset.clientName;

        const registrationDate =
            button.dataset.registrationDate;

        const tariffPk =
            button.dataset.tariffPk;


        document.getElementById(
            "update-record-simcard-pk"
        ).value = pk;

        document.getElementById(
            "IMEI-update-name"
        ).value = imei;

        document.getElementById(
            "Phone-update-name"
        ).value = phone;

        document.getElementById(
            "CustomerName-update-name"
        ).value = clientName;

        document.getElementById(
            "RegDate-update-name"
        ).value = registrationDate;

        document.getElementById(
            "ServiceType-update-name"
        ).value = tariffPk;

        // Updating tariff info popover on update modal open after tariff is applied 
        refreshTariffPopover_upd()


        document.getElementById(
            "updateRecordModalLabel"
        ).textContent =
            `Редактирование записи №${pk}`;
    }
);


// Event on Update Modal Close
updateModal.addEventListener(
    "hide.bs.modal",
    function () {

        if (updateModal.contains(document.activeElement)) {
            document.activeElement.blur();
        }
    }
);


updateModal.addEventListener(
    "hidden.bs.modal",
    function () {

        if (updateModalTrigger) {
            updateModalTrigger.focus();
        }
    }
);

}


function DeleteModalPreccessing() {
    const deleteModal = 
        document.getElementById("deleteRecordModal");

    
    const deleteRecordButton = document.getElementById("submit-delete-record-btn");


    let deleteModalTrigger = null;

    // Event that executes on create modal window show up
    deleteModal.addEventListener(
        "show.bs.modal",
        function (event) {

            const button = event.relatedTarget;

            // For changing focus on modal close
            deleteModalTrigger = button;

            const pk = 
                button.dataset.pk;

            document.getElementById(
                "delete-record-modal-body"
            ).textContent =
                `Вы действительно хотите удалить ${pk}-ую запись?`;
            
            // Assign record pk for deletion
            deleteRecordButton.value = pk;

            
        }
    );


    // Event on Delete Modal Close
    deleteModal.addEventListener(
        "hide.bs.modal",
        function () {

            if (deleteModal.contains(document.activeElement)) {
                document.activeElement.blur();
            }
        }
    );


    deleteModal.addEventListener(
        "hidden.bs.modal",
        function () {

            if (deleteModalTrigger) {
                deleteModalTrigger.focus();
            }
        }
    );

}