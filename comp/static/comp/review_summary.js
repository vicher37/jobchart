        var raw_data = "{{common_words}}";
        console.log(typeof(raw_data));
        raw_data = raw_data.slice(1, -1).split(";,");
        console.log(raw_data);
        console.log(typeof(raw_data));
        console.log(raw_data.length);
        console.log(raw_data[0]);
        var data = [];
        var word_list = [];

        for (var i = 0; i < raw_data.length; i++) {
            node = {}
            console.log(raw_data[i]);
            if (i == raw_data.length - 1) {
                cleaned_obj = raw_data[i].slice(20, -4);
            }
            else {
                cleaned_obj = raw_data[i].slice(20, -3);
            }
            console.log(cleaned_obj);
            freq = parseInt(cleaned_obj.split(",")[3])
            data.push(freq);
            console.log(freq);
            word = cleaned_obj.split(",")[1];
            word_list.push(word);
        }

        var x = d3.scale.linear()
            .domain([0, d3.max(data)])
            .range([0, 420]);

        d3.select(".chart")
          .selectAll("div")
            .data(data)
          .enter().append("div")
            .style("width", function(d) { return x(d) + "px"; })
            .text(function(d) { return d; });
