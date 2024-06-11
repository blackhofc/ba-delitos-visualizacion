export function format(number) {
    // Convert number to string
    let numStr = number.toString();
        
    // Check if number has more than 3 digits
    if (numStr.length > 3) {
        // Insert dot 3 positions from the end
        numStr = numStr.slice(0, -3) + '.' + numStr.slice(-3);
    }
    
    return numStr;
}