class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Use a stack to store all file names separated by /
        """
        stx = []

        for i in path.split("/"):
            # pop stack to return to previous dir
            if i == "..":
                if stx:
                    stx.pop()

            # skip '.' and multiple slashs ('' after split)
            elif i == "." or i == "":
                continue

            # append custom directory names onto stack
            else:
                stx.append(i)

        return "/" + "/".join(stx)  # / at front
