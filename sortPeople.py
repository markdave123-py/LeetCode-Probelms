def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        heightToName = {}

        for i in range(len(names)):
            heightToName[heights[i]] = names[i]

        sortedHeights = sorted(heights, reverse= True)

        sortedNames = []

        for i in range(len(heights)):
            currHeight = sortedHeights[i]
            sortedNames.append(heightToName[currHeight])
        
        return sortedNames
