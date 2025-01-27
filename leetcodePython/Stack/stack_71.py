class Solution:
    def simplifyPath(self, path: str) -> str:
        pathDirectory = []
        PATH_SPLIT = "/"
        PARENT = ".."
        directories = path.split(PATH_SPLIT)
        skipSet = {"", ".", ".."} # refers to root ".."

        for directory in directories:
            if pathDirectory and directory == PARENT: # refers to mid ".."
                pathDirectory.pop()
            elif directory not in skipSet:
                pathDirectory.append(directory)

        return PATH_SPLIT + PATH_SPLIT.join(pathDirectory)

"""
71. Simplify Path
You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

A single period '.' represents the current directory.
A double period '..' represents the previous/parent directory.
Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
The simplified canonical path should follow these rules:

The path must start with a single slash '/'.
Directories within the path must be separated by exactly one slash '/'.
The path must not end with a slash '/', unless it is the root directory.
The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
Return the simplified canonical path.

Example 1:
Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:
Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

Example 3:
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

Example 4:
Input: path = "/a/./b/../../c/"
Output: "/c"

Constraints:
1 <= path.length <= 3000
path consists of English letters, digits, period '.', slash '/', or '_'.
path is a valid absolute Unix path.

------------------------------------------------------------------
Trailing Slash Removal:
    A trailing slash at the end of the path should be removed (e.g., /home/ becomes /home).

Multiple Consecutive Slashes:
    Multiple consecutive slashes should be replaced by a single slash (e.g., /home//foo/ becomes /home/foo).

Parent Directory (..):
    A double period .. refers to moving up one level (parent directory). It should be resolved accordingly (e.g., /home/user/Documents/../Pictures becomes /home/user/Pictures).

Root Directory Constraint:
    Attempting to move above the root directory (e.g., /../) results in staying at the root (/).

Special Directory Names:
    Names like ... are treated as valid directory names and are not interpreted as special symbols (e.g., /.../a/../b/c/../d/./ becomes /.../b/d).

Valid Absolute Unix Path:
    The input path is always a valid absolute Unix path, consisting of English letters, digits, periods ., slashes /, or underscores _.
    
"""