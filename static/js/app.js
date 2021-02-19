function buildMetadata(year) {
    var url = `/data/${year}`;
    // Find the url for 
    d3.json(url).then(function(response) {
      // select the panel with id of `#sample-metadata`
      var metadata_panel = d3.select("#sample-metadata");
      // clear existing metadata cache
      metadata_panel.html("");
      
      // Use `Object.entries` to add each key and value pair to the panel
      Object.entries(response).forEach(function([key, value]) {      
        // append one table row `tr` for each key,value pair 
        var row = metadata_panel.append("tr");
        
        // create collumns
        var cell = row.append("td");
        
        // fill in each cell with text
        cell.text(`${key}: ${value}`);
      });
    });
  }
  
  
  
  function init() {
    // Grab a reference to the dropdown select element
    var selector = d3.select("#selDataset");
  
    // Use the list of sample names to populate the select options
    d3.json("/years").then((sampleNames) => {
      sampleNames.forEach((sample) => {
        selector
          .append("option")
          .text(sample)
          .property("value", sample);
      });
  
      // Use the first sample from the list to build the initial plots
      const firstSample = sampleNames[0];
      buildMetadata(firstSample);
    });
  }
  
  
  function optionChanged(newSample) {
    // Fetch new data each time a new sample is selected
    buildMetadata(newSample);
  }
  
  
  // Initialize the dashboard
  init();