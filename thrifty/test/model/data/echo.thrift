enum ProcessState {
    NOT_CREATED,
    RUNNING,
    STOPPING
}

struct ProcessResult {
    1: ProcessState state,
    2: i32 exitCode
}

exception ProcessError {
    1: string message,
    2: string stack
}

/**
 * An awesome service
 * is an awesome service.
 */
service ProcessExecution {
    /**
     * Process the result
     */
    ProcessResult processThing(1: ProcessResult result) throws (1: ProcessError error),

    /**
     * Execute a thing on the server.
     */
    ProcessResult executeThing(1: string what,
                               2: string node) throws (1: ProcessError error)
}
