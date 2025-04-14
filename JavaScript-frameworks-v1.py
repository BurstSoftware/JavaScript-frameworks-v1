import streamlit as st

# Define all 1,000 items categorized into 8 groups
all_items = {
    "Front-End Libraries and Tools": [
        "React", "Vue.js", "Angular", "Svelte", "Ember.js", "Preact", "Alpine.js", "Solid.js", "Lit",
        "react-dom", "vue", "@angular/core", "svelte", "preact", "solid-js", "lit", "alpinejs", "ember-source",
        "react-router-dom", "@vue/router", "@angular/router", "history", "react-query", "swr", "emotion",
        "styled-components", "@mui/material", "antd", "bootstrap", "tailwindcss", "@headlessui/react",
        "framer-motion", "popmotion", "react-spring", "react-hook-form", "formik", "redux", "@reduxjs/toolkit",
        "mobx", "zustand", "jotai", "recoil", "react-transition-group", "react-bootstrap", "semantic-ui-react",
        "vuetify", "quasar", "@chakra-ui/react", "react-aria", "downshift", "react-select", "floating-ui",
        "tippy.js", "sweetalert2", "react-toastify", "react-dnd", "sortablejs", "react-virtualized", "react-table",
        "ag-grid", "tanstack-table", "react-draggable", "react-resizable", "react-grid-layout", "react-helmet",
        "next-seo", "vue-meta", "react-visibility-sensor", "react-collapse", "react-collapse-pane", "react-player",
        "video.js", "plyr", "react-image", "react-lazyload", "react-parallax", "react-flip-toolkit", "react-move",
        "react-animations", "react-countup", "react-number-format", "react-input-mask", "react-autosuggest",
        "react-typeahead", "react-mentions", "react-tooltip", "react-scroll", "react-smooth-scroll",
        "react-anchor-link-smooth-scroll", "react-infinite-scroll-component", "react-virtual", "react-window",
        "react-paginate", "react-data-grid", "react-sortable-hoc", "react-draggable-list", "react-flip-move",
        "react-animated-css", "react-swipeable", "react-swipeable-views", "react-touch", "react-gesture-responder",
        "react-hotkeys", "react-keyboard-event-handler", "react-shortcuts", "react-hotkeys-hook", "react-focus-lock",
        "react-trap-focus", "react-a11y", "react-aria-modal", "react-overlays", "react-portal", "react-popper-tooltip",
        "react-tiny-popover", "react-confirm-alert", "react-notifications-component", "react-sticky", "react-stickynode",
        "react-visibility", "react-on-screen", "react-appear", "react-awesome-reveal", "react-motion",
        "react-animated-number", "react-count-to", "react-marquee", "react-hover", "react-hover-observer",
        "react-click-outside", "react-outside-click-handler", "react-copy-to-clipboard", "react-clipboard.js",
        "react-download-link", "react-file-download", "react-share", "react-social-icons", "react-fittext",
        "react-textfit", "react-lines-ellipsis", "react-text-truncate", "react-ellipsis-text", "react-clamp-lines",
        "react-textarea-autogrow", "react-autogrow-textarea", "react-expandable-textarea", "react-autoresize-textarea",
        "react-progress-bar", "react-circular-progressbar", "react-step-progress-bar", "react-gauge-chart",
        "react-meter", "react-timer-hook", "react-countdown", "react-timeago", "react-moment", "react-date-picker",
        "react-breakpoints", "react-media", "react-responsive-media", "react-device-detect", "react-browser-detect",
        "react-screen-size", "react-dimension", "react-size-me", "react-measure", "react-sizeme", "react-orientation",
        "react-device-orientation", "react-fullscreen", "react-full-screen", "react-visibility-toggle", "react-show",
        "react-toggle-display", "react-collapse-height", "react-slide-toggle", "react-expander"
    ],
    "Back-End and Server-Side Tools": [
        "Express.js", "NestJS", "Koa.js", "Fastify", "Hapi.js", "AdonisJS", "express", "@nestjs/core", "koa",
        "fastify", "hapi", "socket.io", "axios", "passport", "cors", "helmet", "morgan", "body-parser", "multer",
        "express-session", "cookie-parser", "ws", "http-errors", "serve-static", "node-cron", "bull", "knex",
        "sequelize", "typeorm", "pg", "mysql2", "redis", "ioredis", "dotenv", "express-rate-limit", "connect-redis",
        "express-validator", "node-cache", "lru-cache", "basic-auth", "serve-favicon", "request", "got", "undici",
        "socket.io-client", "mqtt", "amqplib", "kafkajs", "agenda", "node-schedule", "sqlite3", "better-sqlite3",
        "drizzle-orm", "objection.js", "express-fileupload", "connect-pg-simple", "express-static-gzip",
        "node-http-proxy", "http-proxy", "node-rest-client", "restify", "node-mime", "node-fetch-cache",
        "fetch-retry", "node-smtp-server", "imap", "node-pop3", "smtp-server", "node-redis", "node-etcd", "consul",
        "node-zookeeper", "node-ldapjs", "ldapjs", "node-sftp-server", "ssh2", "node-ftp", "basic-ftp",
        "node-webdav-server", "node-smb", "node-telnet", "express-async-errors", "express-promise-router",
        "express-pino-logger", "node-apn", "node-gcm", "push.js", "node-notifier", "node-growl", "node-irc",
        "slack-node", "express-slow-down", "express-useragent", "express-device", "node-bandwidth", "node-network",
        "node-portfinder", "node-os-utils", "node-process", "node-cpu-usage", "node-memory-usage", "node-arp",
        "node-ping", "node-traceroute", "node-dns", "node-whois", "node-ipinfo", "node-ip2location", "node-maxmind",
        "node-geoip-lite", "node-timezone", "express-openapi-validator", "express-basic-auth", "express-brute",
        "node-statsd", "node-metrics", "node-prometheus", "node-monitor", "node-uptime", "node-watchdog-timer",
        "node-heartbeat", "node-sysinfo", "node-os-info", "node-hardware", "node-system-info", "node-disk-space",
        "node-filesystem", "node-dirsize", "node-filelist", "node-file-info", "node-path-exists", "node-load",
        "node-stress", "node-benchmark", "node-perf", "node-performance", "node-latency", "node-throughput",
        "node-queue", "node-task-queue", "node-job-queue", "node-worker", "node-thread", "node-parallel",
        "node-concurrent", "node-async-queue", "node-rate", "node-throttle"
    ],
    "Full-Stack Frameworks and Tools": [
        "Next.js", "Nuxt.js", "Meteor", "Remix", "Astro", "Gatsby", "next", "nuxt", "meteor", "remix-run", "astro",
        "gatsby", "@sveltejs/kit", "blitz", "keystone", "strapi", "directus", "graphql-request", "urql",
        "relay-runtime", "sanity", "contentful", "prismic-client", "feathers", "loopback", "sails", "hono", "trpc",
        "openapi-typescript", "swagger-ui-express", "payloadcms", "ghost-sdk", "netlify-cms", "eleventy", "hexo",
        "docz", "storybook", "@storybook/react", "lerna", "turbo", "frontity", "gridsome", "docusaurus", "vuepress",
        "mdx", "gatsby-plugin-mdx", "nextra", "nx", "pnpm", "yalc", "degit", "ncp", "cpx", "recursive-copy",
        "node-archive", "node-compress", "node-decompress", "node-zip", "node-unzip", "node-tar", "node-untar",
        "node-gzip", "node-ungzip", "node-bzip"
    ],
    "Build Tools and Optimizations": [
        "webpack", "@rollup/core", "esbuild", "vite", "parcel", "swc", "babel/core", "@babel/preset-env", "terser",
        "uglify-js", "clean-webpack-plugin", "html-webpack-plugin", "css-loader", "style-loader", "sass", "postcss",
        "autoprefixer", "babel-loader", "compression-webpack-plugin", "workbox", "mini-css-extract-plugin",
        "copy-webpack-plugin", "webpack-bundle-analyzer", "vite-plugin-pwa", "rollup-plugin-terser", "vite-plugin-ssr",
        "rollup-plugin-visualizer", "webpackbar", "speed-measure-webpack-plugin", "critical", "cssnano", "purgecss",
        "postcss-import", "stylelint", "esbuild-jest", "vite-plugin-mdx", "rollup-plugin-postcss", "webpack-assets-manifest",
        "optimize-css-assets-webpack-plugin", "image-webpack-loader", "postcss-flexbugs-fixes", "postcss-normalize",
        "postcss-custom-properties", "esbuild-plugin-import-glob", "vite-plugin-dts", "vite-plugin-svgr",
        "rollup-plugin-dts", "webpack-shell-plugin-next", "webpack-notifier", "postcss-pxtorem", "postcss-scss",
        "postcss-sass", "postcss-less", "esbuild-loader", "vite-plugin-checker", "vite-plugin-html", "rollup-plugin-copy",
        "webpack-merge", "webpack-subresource-integrity", "postcss-color-mod", "postcss-short", "postcss-easing-gradients",
        "postcss-font-magician", "esbuild-plugin-copy", "vite-plugin-compression", "vite-plugin-restart",
        "rollup-plugin-delete", "webpack-log", "webpack-cleanup-plugin", "postcss-merge-longhand", "postcss-merge-rules",
        "postcss-discard-duplicates", "postcss-discard-empty", "esbuild-plugin-clean", "vite-plugin-inspect",
        "vite-plugin-env", "rollup-plugin-json", "webpack-env", "webpack-define-plugin", "postcss-clean",
        "postcss-combine-media-query", "postcss-sort-media-queries", "postcss-reporter", "esbuild-plugin-env",
        "vite-plugin-static-copy", "vite-plugin-legacy", "rollup-plugin-uglify", "webpack-stats-plugin",
        "webpack-progress", "postcss-assets", "postcss-url", "postcss-inline-svg", "postcss-sprites",
        "esbuild-plugin-manifest", "vite-plugin-manifest"
    ],
    "Utility Libraries": [
        "lodash", "underscore", "ramda", "moment", "dayjs", "date-fns", "uuid", "qs", "chalk", "debug", "async",
        "rxjs", "bluebird", "p-limit", "p-queue", "nanoid", "shortid", "validator", "sanitize-html", "deepmerge",
        "clone", "query-string", "memoizee", "fast-json-stable-stringify", "json5", "yaml", "csv-parse", "papaparse",
        "xml2js", "js-yaml", "humanize-duration", "pretty-bytes", "dot-prop", "get-value", "set-value", "object-path",
        "extend", "merge-deep", "strip-json-comments", "jsonfile", "fs-jetpack", "glob", "path-to-regexp", "minimatch",
        "fast-glob", "globby", "mkdirp", "del", "copyfiles", "move-file", "replace-in-file", "temp", "pretty-ms", "ms",
        "filesize", "bytes", "stringify-object", "json-stable-stringify", "strip-ansi", "ansi-colors", "execa",
        "cross-spawn", "isomorphic-fetch", "whatwg-fetch", "url-parse", "querystring", "parseurl", "path-parse",
        "normalize-path", "upath", "file-exists", "is-glob", "is-url", "is-email", "is-ip", "is-uuid", "is-base64",
        "is-json", "is-empty", "is-equal", "is-object", "is-array", "is-number", "is-string", "is-boolean",
        "is-function", "is-date", "is-regexp", "is-null", "is-undefined", "is-def", "is-nil", "to-string", "to-number",
        "to-boolean", "to-array", "to-object", "to-json", "from-json", "clone-deep", "shallow-clone", "merge"
    ],
    "Testing Frameworks and Tools": [
        "jest", "mocha", "chai", "sinon", "cypress", "playwright", "vitest", "supertest", "typescript", "tslib",
        "@types/node", "@types/react", "enzyme", "react-testing-library", "@testing-library/jest-dom", "mockery",
        "nock", "faker", "istanbul", "nyc", "eslint", "husky", "tape", "ava", "jasmine", "karma", "nightmare",
        "testcafe", "codecov", "eslint-plugin-react", "eslint-plugin-import", "rewire", "proxyquire", "sinon-chai",
        "jest-fetch-mock", "react-testing-library", "jest-environment-jsdom", "wdio", "selenium-webdriver",
        "cucumber", "standard", "tslint", "jest-watch-typeahead", "jest-canvas-mock", "jest-axe", "mocha-parallel-tests",
        "chai-as-promised", "mockdate", "nock-back", "eslint-plugin-jsx-a11y", "eslint-plugin-promise",
        "semantic-release", "jest-each", "jest-serializer", "jest-environment-node", "mocha-junit-reporter",
        "chai-subset", "mock-fs", "node-mocks-http", "eslint-plugin-testing-library", "eslint-plugin-sonarjs",
        "prettier-plugin-tailwindcss", "jest-mock-console", "jest-mock-random", "jest-mock-date", "mocha-each",
        "chai-match", "mock-socket", "node-unit", "eslint-plugin-jsdoc", "eslint-plugin-json", "eslint-plugin-md",
        "jest-matcher-utils", "jest-snapshot", "mocha-clean", "chai-arrays", "chai-datetime", "mock-process",
        "node-mock-stdio", "node-test", "eslint-plugin-security", "eslint-plugin-no-unsanitized", "commitlint",
        "tap", "tap-spec", "jest-mock-fn", "jest-mock-object", "jest-mock-promise", "chai-things", "mock-require",
        "node-mock-globals", "eslint-plugin-import-order", "eslint-plugin-no-only-tests"
    ],
    "Data Visualization and Graphics": [
        "d3", "three", "gsap", "chart.js", "recharts", "victory", "nivo", "pixi.js", "paper.js", "apexcharts",
        "highcharts", "plotly.js", "konva", "snap.svg", "billboard.js", "c3", "metrics-graphics", "fabric.js",
        "fusioncharts", "dygraphs", "vis-network", "two.js", "raphael", "chartist", "morris.js", "sigma.js",
        "zrender", "vanta", "flot", "jqplot", "g6", "spritejs", "tween.js", "peity", "sparkline", "d3fc",
        "roughjs", "pizzazz", "britecharts", "cubism", "dc.js", "svg-sprite", "svg-sprite-loader"
    ],
    "Specialized and Niche Tools": [
        "Electron", "Ionic", "React Native", "electron", "ionic", "react-native", "expo", "jsonwebtoken", "bcrypt",
        "mongoose", "prisma", "unocss", "million", "qwik", "fresh", "redwoodjs", "graphql", "@apollo/client",
        "node-fetch", "cross-fetch", "superagent", "fs-extra", "rimraf", "nodemon", "pm2", "concurrently", "prettier",
        "commander", "inquirer", "yargs", "ora", "minimist", "cheerio", "puppeteer", "sharp", "compression",
        "imagemin", "handlebars", "ejs", "pug", "marked", "highlight.js", "node-sass", "crypto-js", "node-rsa",
        "otplib", "pdfkit", "jsdom", "juice", "nodemailer", "mjml", "eta", "nunjucks", "hyperapp", "effector",
        "xstate", "node-qrcode", "jsbarcode", "exceljs", "xlsx", "archiver", "unzipper", "node-watch", "chokidar",
        "twit", "node-ical", "rrule", "node-osc", "midi", "soundjs", "howler.js", "tone.js", "node-hid",
        "serialport", "johnny-five", "node-geoip", "ip", "country-list", "node-geocoder", "opentype.js", "fontkit",
        "node-canvas", "svg.js", "node-uuid-parse", "node-randomstring", "node-string", "node-text", "node-encode",
        "node-decode", "node-escape", "node-unescape", "node-trim", "node-pad", "node-slug", "node-token",
        "node-uid", "node-id", "node-uniqid", "node-hashid", "node-secure-random", "node-rand", "node-seed",
        "node-shuffle", "crypto", "node-uuid", "html-to-text", "js-beautify", "html-minifier", "node-exif", "gm",
        "probe-image-size", "node-hash", "node-base64", "node-hex", "node-binary", "node-buffer", "node-random",
        "node-timers", "node-time", "node-cron-parser"
    ],
    "Emerging or Niche Frameworks": [
        "Backbone.js", "Knockout.js", "Mithril", "Qwik", "hyperapp", "alpine", "redom", "nanohtml", "bel", "yo-yo",
        "morphdom", "reef", "omi", "cyclejs", "choo", "nanomorph", "vhtml", "hdom", "nano-jsx", "petit-dom",
        "dommy", "lit-element", "haunted", "fast", "uhtml", "domdiff", "nano-id", "nano-css", "nano-component",
        "nano-events", "nano-state", "lemonadejs", "stimulus", "marko", "lit-html", "swup", "petite-vue",
        "svelte-preprocess", "sapper"
    ]
}

# Streamlit app
def main():
    # Title of the app
    st.title("JavaScript Frameworks, Packages, and Modules Explorer")

    # Dropdown for selecting category at the top
    category = st.selectbox(
        "Select a Category",
        options=list(all_items.keys()),
        index=0  # Default to the first category
    )

    # Display the list of items based on the selected category
    st.subheader(f"Items in {category}")
    for item in all_items[category]:
        st.write(f"- {item}")

if __name__ == "__main__":
    main()
