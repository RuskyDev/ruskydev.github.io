// Function to fetch member count for Thunder Rayz server
function fetchThunderRayzMemberCount() {
    fetch('http://localhost:3000/guildid=1016234559874015252')
      .then(response => response.json())
      .then(data => {
        const memberCount = data.memberCount;
        document.getElementById('thunderRayzMemberCount').textContent = memberCount;
      })
      .catch(error => console.error(error));
  }
  
  // Function to fetch member count for Masked Psycho Community server
  function fetchMaskedPsychoMemberCount() {
    fetch('http://localhost:3000/guildid=997185907079790732')
      .then(response => response.json())
      .then(data => {
        const memberCount = data.memberCount;
        document.getElementById('maskedPsychoMemberCount').textContent = memberCount;
      })
      .catch(error => console.error(error));
  }
  
  // Function to fetch member count for RedBird server
  function fetchRedBirdMemberCount() {
    fetch('http://localhost:3000/guildid=1054257818045267978')
      .then(response => response.json())
      .then(data => {
        const memberCount = data.memberCount;
        document.getElementById('redBirdMemberCount').textContent = memberCount;
      })
      .catch(error => console.error(error));
  }
  
  // Call the functions to fetch member counts
  fetchThunderRayzMemberCount();
  fetchMaskedPsychoMemberCount();
  fetchRedBirdMemberCount();
  