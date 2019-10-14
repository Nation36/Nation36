new Vue ({
  el: '#app',
  delimiters: ['[[', ']]'],
  data: {
    csrf_token: document.querySelector("input[name=csrfmiddlewaretoken]").value,
    map_data: null,
    objs: [],
    new_layout: {
      obj: null,
      x_position: null,
      y_position: null
    },
    background_file: null,
    obj_one: null,
    obj_two: null,
    selected_obj: null,
    layout_count: 0,
  },
  methods: {
    select_obj (obj) {
      this.selected_obj = obj;
      console.log(this.selected_obj)
    },
    place_obj (obj, tile) {
      let selected_tile = document.getElementById(tile);
      let image = document.createElement('img');
      image.src = obj.appearance;
      image.width = '73';
      image.height = '73';
      selected_tile.innerHTML = '';
      selected_tile.appendChild(image);
      let pos = tile.split('-');
      console.log(this.map_data.layout_set);
      this.new_layout.y_position = pos[0];
      this.new_layout.x_position = pos[1];
      this.new_layout.obj = obj;
      this.map_data.layout_set[this.layout_count] = this.new_layout;
      this.layout_count++;
      console.log(this.new_layout);
      console.log(this.map_data.layout_set);
    },
    submit() {
      axios ({
        url: '../api/maps/',
        method: 'post',
        headers: {
          'X-CSRFToken': this.csrf_token
        },
        data: this.map_data,
      }).then(res => console.log(res.data))
    },
  },
  mounted () {
    axios ({
      url: '../api/maps/',
      method: 'get',
      headers: {
        'X-CSRFToken': this.csrf_token
      },
    }).then(res => {
      this.map_data = res.data.results[0];
      this.background_file = this.map_data.background.toString();
      this.background_file = this.background_file.split("\\");
      this.background_file.reverse();
      this.background_file = this.background_file[0];
      this.background_file = '/static/'+this.background_file;
    }
    );
    axios ({
      url: '../api/objs/',
      method: 'get',
      headers: {
        'X-CSRFToken': this.csrf_token
      },
    }).then(res => {
      this.objs = res.data.results;
      this.obj_one = this.objs[0];
      this.obj_two = this.objs[1];
    })
  }
})
