let isSideColumnVisibleByUser = true;

function alignSideColumn() {
    const mainColumn = document.getElementById('main-column');
    const sideColumn = document.getElementById('side-column');
    const header = document.getElementById('header');
    const headerHeight = header.getBoundingClientRect().height;
    sideColumn.style.top = (headerHeight + 10) + 'px';
}

function addFloatingStyles() {
    const sideColumn = document.getElementById('side-column');
    sideColumn.classList.remove('static', 'relative');
    sideColumn.classList.add('fixed', 'z-50', 'shadow-lg', 'rounded-lg');
    sideColumn.style.left = '10px';
    sideColumn.style.maxWidth = '280px';
}

function removeFloatingStyles() {
    const sideColumn = document.getElementById('side-column');
    sideColumn.classList.remove('fixed', 'z-50', 'shadow-lg', 'rounded-lg');
    sideColumn.classList.add('static');
    sideColumn.style.left = '';
    sideColumn.style.top = '';
    sideColumn.style.maxWidth = '';
}

document.getElementById('hide-btn').addEventListener('click', function() {
    this.classList.add('hidden');
    document.getElementById('move-btn').classList.remove('hidden');
    addFloatingStyles();
    alignSideColumn();
    document.getElementById('side-column').style.display = 'none';
    document.getElementById('main-column').classList.remove('ml-8');
    document.getElementById('hamburger-btn').classList.remove('hidden');
    isSideColumnVisibleByUser = false;
});

document.getElementById('move-btn').addEventListener('click', function() {
    this.classList.add('hidden');
    document.getElementById('hide-btn').classList.remove('hidden');
    removeFloatingStyles();
    document.getElementById('side-column').style.display = '';
    document.getElementById('main-column').classList.add('ml-8');
    document.getElementById('hamburger-btn').classList.add('hidden');
    isSideColumnVisibleByUser = true;
});

document.getElementById('hamburger-btn').addEventListener('click', function() {
    const sideColumn = document.getElementById('side-column');
    const mainColumn = document.getElementById('main-column');
    if (sideColumn.style.display === 'none' || sideColumn.style.visibility === 'hidden') {
        sideColumn.style.display = '';
        sideColumn.style.visibility = 'visible';
        mainColumn.classList.add('ml-8');
        isSideColumnVisibleByUser = true;
    } else {
        sideColumn.style.display = 'none';
        sideColumn.style.visibility = 'hidden';
        mainColumn.classList.remove('ml-8');
        addFloatingStyles();
        document.getElementById('move-btn').classList.remove('hidden');
        document.getElementById('hide-btn').classList.add('hidden');
        isSideColumnVisibleByUser = false;
    }
});

function handleResize() {
    const sideColumn = document.getElementById('side-column');
    const mainColumn = document.getElementById('main-column');
    const hamburgerBtn = document.getElementById('hamburger-btn');
    
    if (window.innerWidth < 768) {
        // Mobile view
        addFloatingStyles();
        sideColumn.style.display = 'none';
        mainColumn.classList.remove('ml-8');
        hamburgerBtn.classList.remove('hidden');
        document.getElementById('hide-btn').classList.add('hidden');
        document.getElementById('move-btn').classList.remove('hidden');
    } else {
        // Desktop view
        if (isSideColumnVisibleByUser) {
            removeFloatingStyles();
            sideColumn.style.display = '';
            sideColumn.style.visibility = 'visible';
            mainColumn.classList.add('ml-8');
            hamburgerBtn.classList.add('hidden');
            document.getElementById('hide-btn').classList.remove('hidden');
            document.getElementById('move-btn').classList.add('hidden');
        }
    }
}

window.addEventListener('resize', handleResize);

window.addEventListener('resize', function() {
    const sideColumn = document.getElementById('side-column');
    if (sideColumn.classList.contains('fixed')) {
        alignSideColumn();
    }
});

window.addEventListener('scroll', function() {
    const sideColumn = document.getElementById('side-column');
    if (sideColumn.classList.contains('fixed')) {
        alignSideColumn();
    }
});

window.onload = function() {
    handleResize();
};
