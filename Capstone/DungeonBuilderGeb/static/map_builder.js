new Vue ({
  el: '#app',
  delimiters: ['[[', ']]'],
  data: {
    csrf_token: document.querySelector("input[name=csrfmiddlewaretoken]").value,
    map_data: null,
    new_map: {
      author: null,
      background: null,
      name: null,
      layout_set: []
    }
  },
  methods: {
    create: function() {
      axios({
        url: 'api/maps/',
        method: 'post',
        headers: {
          'X-CSRFToken': this.csrf_token
        },
        data: this.new_map
      }).then(res => window.location.assign("http://localhost:8000/new-map/layout"))
    },
    set_background: function(selected_background, user_id) {
      this.new_map.background = selected_background
      this.new_map.author = user_id
    },
  },
  mounted () {
    axios({
      url: 'api/maps/',
      method: 'get',
      headers: {
        'X-CSRFToken': this.csrf_token
      }
    }).then(res => this.map_data = res.data.results)
  }
})
