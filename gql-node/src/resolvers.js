export const resolvers = {
  Query: {
    name (root, args, context, info) {
      return 'Lewis Rodgers';
    },
    alias (root, {heroName}, context, info) {
      console.log(context);
      return heroName;
    },
  },
};