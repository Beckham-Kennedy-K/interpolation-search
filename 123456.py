INTERPOLATION_SEARCH(arr, target)

    low ← 0
    high ← length(arr) - 1

    WHILE low ≤ high AND target ≥ arr[low] AND target ≤ arr[high]:

        IF arr[high] = arr[low] THEN
            IF arr[low] = target THEN
                RETURN low
            ELSE
                RETURN -1
            END IF
        END IF

        // Interpolation formula to estimate probe position
        pos ← low + ((target - arr[low]) × (high - low)) / (arr[high] - arr[low])
        pos ← FLOOR(pos)

        IF arr[pos] = target THEN
            RETURN pos

        ELSE IF arr[pos] < target THEN
            low ← pos + 1

        ELSE
            high ← pos - 1
        END IF

    END WHILE

    RETURN -1      // Element not found
