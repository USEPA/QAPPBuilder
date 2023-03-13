
function SectionBTypeChanged(e) {
    let val = $(e).val();
    console.log(val);
    // TODO Reload this page with a form for the selected section b type
    let href = window.location.href;
    if (href.includes('sectionb_type')) {
        href = href.replace(/sectionb_type=[0-9]{1,}/, 'sectionb_type=' + val);
    } else {
        href = href + '&sectionb_type=' + val;
    }
    window.location.href = href;
}

//////////////////////////////////////////////////////////////////////
// Project Lead Section
function addProjectLead(id) {
    window.location.href = '/project_lead/create?qapp_id=' + id;
}

function getId(btn) {
    var split = $(btn).attr('id').split('-');
    var id = split[0];
    if (split.length > 1)
        id = split[1];
    return id
}

function editProjectLead(btn) {
    if ($(btn).attr('disabled')) return;
    window.location.href = '/project_lead/edit/' + getId(btn);
}

function removeProjectLead(btn) {
    if ($(btn).attr('disabled')) return;
    window.location.href = '/project_lead/delete/' + getId(btn);
}

//////////////////////////////////////////////////////////////////////
// Project Approval Section
function editApprovalPage(id) {
    window.location.href = '/approval/edit/' + id;
}
//////////////////////////////////////////////////////////////////////
// Project Approval Signature Section
function addApprovalSignature(id) {
    window.location.href = '/approval_signature/create?qapp_id=' + id;
}

function editApprovalSignature(btn) {
    if ($(btn).attr('disabled')) return;
    window.location.href = '/approval_signature/edit/' + getId(btn);
}

function removeApprovalSignature(btn) {
    if ($(btn).attr('disabled')) return;
    window.location.href = '/approval_signature/delete/' + getId(btn);
}
//////////////////////////////////////////////////////////////////////