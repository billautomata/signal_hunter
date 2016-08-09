module.exports = function (grunt) {

  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-browserify')
  grunt.loadNpmTasks('grunt-standard')

  grunt.registerTask('default','watch')

  grunt.initConfig({

    browserify: {
      main: {
        src: 'public/src/main.js',
        dest: 'public/build/bundle.js',
        files: {
          'public/build/bundle.js': ['./public/src/*.js'],
        },
        options: {
          transform: ['brfs']
        }
      }
    },
    // standard linting
    standard: {
      main: {
        options: {
          format: true,
          lint: true
        },
        src: [
          './public/src/*.js'
        ]
      }
    },
    watch: {
      everything: {
        files: ['./public/*.html','./public/src/*.js', './public/css/*.css' ],
        tasks: ['standard', 'browserify'],
        options: {
          livereload: {
            port: 35729,
            // key: grunt.file.read('nginx.key'),
            // cert: grunt.file.read('nginx.crt')
            // you can pass in any other options you'd like to the https server, as listed here: http://nodejs™.org/api/tls.html#tls_tls_createserver_options_secureconnectionlistener
          }
        },
      },
    }
  })
}
