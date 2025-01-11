module.exports = function (eleventyConfig) {
    // Copy assets directory
    eleventyConfig.addPassthroughCopy("src/assets");

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
