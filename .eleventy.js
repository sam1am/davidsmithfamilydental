module.exports = function (eleventyConfig) {
    // Copy assets directory (except CSS) and favicon
    eleventyConfig.addPassthroughCopy({
        "src/assets/images": "assets/images",
        "src/favicon.ico": "favicon.ico"
    });

    // Add groupBy filter
    eleventyConfig.addFilter("groupBy", function(array, key) {
        return array.reduce((groups, item) => {
            const group = (groups[item[key]] || []);
            group.push(item);
            groups[item[key]] = group;
            return groups;
        }, {});
    });

    return {
        dir: {
            input: "src",
            output: "docs",
            includes: "_includes"
        }
    };
};
