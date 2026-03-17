let isSideColumnVisibleByUser = true;

function alignSideColumn() {
    const mainColumn = document.getElementById('main-column');
    const sideColumn = document.getElementById('side-column');
    const mainColumnTop = mainColumn.getBoundingClientRect().top + window.scrollY;
    sideColumn.style.top = mainColumnTop + 'px';
}

document.getElementById('hide-btn').addEventListener('click', function() {
    this.classList.add('hidden');
    document.getElementById('move-btn').classList.remove('hidden');
    document.getElementById('side-column').classList.add('floating');
    alignSideColumn();
    document.getElementById('side-column').style.visibility = 'hidden';
    document.getElementById('hamburger-btn').classList.remove('hidden');
isSideColumnVisibleByUser = false;
});

document.getElementById('move-btn').addEventListener('click', function() {
    this.classList.add('hidden');
    document.getElementById('hide-btn').classList.remove('hidden');
    document.getElementById('side-column').classList.remove('floating');
    document.getElementById('side-column').style.visibility = 'visible';
    document.getElementById('hamburger-btn').classList.add('hidden');
isSideColumnVisibleByUser = true;
});

document.getElementById('hamburger-btn').addEventListener('click', function() {
    var sideColumn = document.getElementById('side-column');
    if (sideColumn.style.visibility === 'hidden') {
	sideColumn.style.visibility = 'visible';
  isSideColumnVisibleByUser = true;
    } else {
	sideColumn.style.visibility = 'hidden';
	sideColumn.classList.add('floating');
	document.getElementById('move-btn').classList.remove('hidden');
	document.getElementById('hide-btn').classList.add('hidden');
  isSideColumnVisibleByUser = false;
    }
});

function handleResize() {
  if (window.innerWidth < 768) {
    document.getElementById('side-column').classList.add('floating');
    document.getElementById('side-column').style.visibility = 'hidden';
    document.getElementById('hamburger-btn').classList.remove('hidden');
  } else {
    if (isSideColumnVisibleByUser) {
      document.getElementById('side-column').classList.remove('floating');
      document.getElementById('side-column').style.visibility = 'visible';
      document.getElementById('hamburger-btn').classList.add('hidden');
    }
  }
}

window.addEventListener('resize', handleResize);

window.addEventListener('resize', function() {
      if (document.getElementById('side-column').classList.contains('floating')) {
	  alignSideColumn();
      }
  });

  window.addEventListener('scroll', function() {
      if (document.getElementById('side-column').classList.contains('floating')) {
	  alignSideColumn();
      }
  });

window.onload = function() {
  handleResize();
};
