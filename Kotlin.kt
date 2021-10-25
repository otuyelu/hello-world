fun main() {
    // variable declared with val are treated as constants
    // their values can not be changed later
    val age = 11
    var ageInDays = age * 365
    val name = "Ayomikun"
    println("Happy Birthday, ${name}!")
    
    // Let's print a cake!
    println("   ,,,,,   ")
    println("   |||||   ")
    println(" =========")
    println("@@@@@@@@@@@")
    println("{~@~@~@~@~}")
    println("@@@@@@@@@@@")
    
    // This prints an empty line.
    println("")

    println("${name}, You are already ${age} years that is ${ageInDays} days old!")
    println("${age} is the very best age to celebrate!")
}
