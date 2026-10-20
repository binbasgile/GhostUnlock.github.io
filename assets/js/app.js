// Simple vanilla JS for frontend interactivity without heavy frameworks needed initially
document.addEventListener('DOMContentLoaded', function() {
    
    const imeiInput = document.getElementById('imei-input'); 
    const submitBtn = document.getElementById('submit-btn'); // Assuming button ID
    
    if(submitBtn && imeiInput){
        
        submitBtn.addEventListener('click', async () => {
            
            let imeiVal = imeiInput.value.replace(/[^A-Z0-9]/g, ''); 
            
            if(imeiVal.length < 14 || imeiVal.length > 17) {
                alert("IMEI must be between 14 and 17 characters (e.g., IMEI or ESN for iPhones).");
                return;
            }

            const btnText = submitBtn.innerText; 
            submitBtn.disabled = true; // Prevent double click
            
            try{
                console.log(`Sending request to /api/v1/unlock with: ${imeiVal}`); 
                
                // Simulate API call response (In prod this would fetch('/api/v1/unlock', ...))
                
                setTimeout(() => {
                    if(Math.random() > 0.2) { // Random success chance simulating backend logic
                        alert("Unlock process started! Check status below.");
                        
                        updateStatusUI({status: 'processing', text: "Connecting via Proxy Pool..."});
                    } else {
                         throw new Error("Proxy connection failed");
                    }

                }, 500); 

            } catch(err){
                alert(`Error: ${err.message}`); 
                submitBtn.disabled = false; 
            }

        });

    } 
    
});

// Helper to simulate UI updates based on API response (JSON structure from FastAPI)
function updateStatusUI(dataObj){
    const box = document.getElementById('status-box'); // Target element
    
    if(!box) return; // Fallback if ID mismatch in HTML template
    
    box.innerHTML = `<strong>${dataObj.text || "Processing..."}</strong><br/>`; 
    
    // Dynamic styling based on status
    let colorClass = ""; 
    let textColor="#c9d1d9";
    
    if(dataObj.status === 'completed') { 
         colorClass="success-box"; textColor="white"; }
     else if(dataObj.status === 'error') { colorClass="error-box"; textColor="#da3633";}

     box.className += " "+colorClass; // Append class for animation triggers
}
