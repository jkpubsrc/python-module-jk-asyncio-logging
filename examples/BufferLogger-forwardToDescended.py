#!/usr/bin/python3



import asyncio
import os

from jk_asyncio_logging import *



async def main():

	clog = AsyncioConsoleLogger.create(logMsgFormatter=COLOR_LOG_MESSAGE_FORMATTER)

	blog = AsyncioBufferLogger.create()

	await blog.info("First we write something to a buffer.")
	await blog.info("And something more.")
	await blog.notice("And more.")
	await blog.debug("And even more.")
	await blog.warn("And even a warning.")
	await blog.info("Soon we'll forward all this to the console.")
	await blog.forwardToDescended(clog, "This is a test.")

#





#asyncio.run(main())									# since python 3.7
asyncio.get_event_loop().run_until_complete(main())		# till python 3.6











