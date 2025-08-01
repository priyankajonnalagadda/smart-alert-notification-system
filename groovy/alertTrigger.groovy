// @Grab(group='commons-collections', module='commons-collections', version='3.2.1')
// @Grab(group='commons-lang', module='commons-lang', version='2.4')
// @Grab(group='org.codehaus.groovy.modules.http-builder', module='http-builder', version='0.7.1')

import groovy.json.JsonSlurper
import groovy.json.JsonOutput


// Simulated incoming event
def incomingEvent = [
    service: "PaymentGateway",
    severity: "CRITICAL",
    message: "Transaction failure rate exceeded threshold"
]

// Load alert rules
def rulesFile = new File("../python/config/alert_rules.json")
def rules = new JsonSlurper().parseText(rulesFile.text)

// Check if event matches any alert rule
def shouldAlert = rules.any { rule ->
    incomingEvent.service == rule.service && incomingEvent.severity == rule.severity
}

if (shouldAlert) {
    println "ALERT TRIGGERED: ${incomingEvent.message}"
    def payload = JsonOutput.toJson(incomingEvent)
    
    // Simulate publishing to Python SNS handler (call to REST endpoint placeholder)
    println "Sending alert payload to SNS handler..."
    println payload
} else {
    println "No matching rule — event ignored."
}
