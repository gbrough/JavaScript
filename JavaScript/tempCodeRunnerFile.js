    const result = []
    for (let i = 0; i < 0; i++) {
        let num = nums[i]
        let idx = index[i]

        result.splice(idx, 0, num)
    }
    return result
};