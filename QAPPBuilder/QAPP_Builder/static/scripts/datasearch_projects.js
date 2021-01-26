// Shared JS Functions for the Projects module.

function clearSelList(id) {
    $(id).empty();
    $(id).append('<option value selected>---------</option>');
}

function addToSelList(id, val, txt) {
    $(id).append('<option value="' + val + '">' + txt + '</option>');
}

function populateSelectGeneric(selId, url) {
    $.ajax({
        url: url,
        success: function (data) {
            for (c in data) {
                addToSelList(selId, data[c]['id'], data[c]['name']);
            }
        },
        error: function (e) {
            console.log(e);
        }
    });
}

function populateCentersOffices(e) {
    let selId = '#id_center_office';
    clearSelList(selId);
    let url = '/projects/api/centers/' + e.target.value;
    populateSelectGeneric(selId, url);
    // Clear out all children selects (important for edit):
    clearSelList('#id_division');
    clearSelList('#id_branch');
}

function populateDivisions(e) {
    let selId = '#id_division';
    clearSelList(selId);
    let url = '/projects/api/divisions/' + e.target.value;
    populateSelectGeneric(selId, url);
    // Clear out all children selects (important for edit):
    clearSelList('#id_branch');
}

function populateBranches(e) {
    let selId = '#id_branch';
    clearSelList(selId);
    let url = '/projects/api/branches/' + e.target.value;
    populateSelectGeneric(selId, url);
}