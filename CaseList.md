##Age
1. `case_rfc2616_stale-ageWarning113.yaml`
    > cache MUST attach Warning 113 to hits older than 1day

2. `case_rfc2616_largeAge-30len.yaml`
    > cache MUST handle 30-length age or transmit 2147483648

3. `case_rfc2616_age-include.yaml`
    > from-cache responses MUST include an Age header

4. `case_rfc2616_age-0s-noResp-noReq-delay.yaml`
    > When using 0-second origin age header with no response delay and no request delay, cache MUST return 0 age

5. `case_rfc2616_age-40s-noResp-noReq-delay.yaml`
    > When using 0-second origin age header with no response delay and no request delay, cache MUST return 40 age

6. `case_rfc2616_age-5100s-3sResp-4sReq-delay.yaml`
    > When using 0-second origin age header with 3 second response delay and 4 second request delay, cache MUST return 5107 age

7. `case_rfc2616_age-169600s-noResp-noReq-delay.yaml`
    > When using 0-second origin age header with no response delay and no request delay, cache MUST return 169600 age

8. `case_rfc2616_age-31536005s.yaml`
    > cache MUST handle 31536005 age

9. `case_rfc2616_age-1073741823s.yaml`
    > cache MUST handle 1073741823s age

10. `case_rfc2616_age-2147483647s.yaml`
    > cache MUST handle 2147483647 age

11. `case_rfc2616_age-2147483648s.yaml`
    > cache MUST handle 2147483648s age

12. `case_rfc2616_age-2147483649s.yaml`
    > cache MUST handle 2147483649s age, then transmit 2147483648

13. `case_rfc2616_age-noAge-noResp-5sReq-delay.yaml`
    > When using no age header with no response delay and 5 second request delay, cache MUST return 5 age

14. `case_rfc2616_age-noAge-noResp-noReq-delay.yaml`
    > When using no age header with no response delay and no request delay, cache MUST return 0 age

15. `case_rfc2616_largeAge-55len.yaml`
    > cache MUST handle 55-length age, then transmit 2147483648

16. `case_rfc2616_largeAge-111len.yaml`
    > cache MUST handle 111-length age, then transmit 2147483648

17. `case_rfc2616_resp_add-missing-date.yaml`
    >  proxy MUST add missing Date header to response

18. `case_rfc2616_stale-ageWarning113-cache-5s.yaml`
    > cache MUST attach Warning 113 to hits older than 86405 seconds cached for 5 seconds

##Cache-Control
###Request
1. `case_rfc2616_ReqCC-no-cache-respFrom.yaml`
    > Cache MUST not use entity in cache if request with cache-control=no-cache

2. `case_rfc2616_ReqPragma-no-cache-respFrom.yaml`
    > Cache MUST not use entity in cache if request with Pragma=no-cache

3. `case_rfc2616_Reqcc-max-stale-warning-110.yaml`
    > cache MUST attach a Warning 110 (Response is Stale) header if stale

4. `case_rfc2616_nocache-Req-no-store.yaml`
    > Cache MUST NOT cache the response if the request is with cache-control: no-store

5. `case_rfc2616_ReqCC-no-store.yaml`
    > Cache MUST NOT use the copy in cache if request with cache-control: no-store

6. `case_rfc2616_ccReqDirMsg-min-fresh-Cache-Control.yaml`
    Cache MUST not use entity in cache if request with cache-control=min-fresh
         
###Response
1. `case_rfc2616_Respcc-nocacheNoExp.yaml`
    > Cache MUST revalidate cache entity with cache-control: no-cache and without expire time

2. `case_rfc2616_Respcc-nocachewithExp.yaml`
    > Cache MUST revalidate cache entity with cache-control: no-cache and expire time

3. `case_rfc2616_Respcc-stale-smaxage0.yaml`
    > Cache MUST revalidate the cached entity whose s-maxage=0

4. `case_rfc2616_Respcc-stale-smaxage8.yaml`
    > Cache MUST revalidate the cached entity whose s-maxage=8

5. `case_rfc2616_Respcc-maxageAndExp.yaml`
    > Cache MUST cache the response if the response header with maxage and expires

6. `case_rfc2616_Respcc-maxageOnly.yaml`
    > Cache MUST cache the response if the response header with maxage only

7. `case_rfc2616_Respcc-must-revalidate.yaml`
    > Cache MUST cache the response if the response header with must-revalidate only

8. `case_rfc2616_Respcc-no-store.yaml`
    > Cache MUST cache the response if the response header with no-store only

9. `case_rfc2616_Respcc-privateOnly.yaml`
    > Cache MUST cache the response if the response header with private only

10. `case_rfc2616_Respcc-proxy-revalidate.yaml`
    > Cache MUST cache the response if the response header with proxy-revalidate only

11. `case_rfc2616_Respcc-RespMaxageFresh-ReqMaxageAsStale.yaml`
    > Cache MUST cache the response if the response maxage and request maxage

12. `case_rfc2616_Respcc-RespMaxageStale-ReqMaxageAsFresh.yaml`
    > Cache MUST cache the response if the request maxage and response maxage

13. `case_rfc2616_Respcc-Smaxage-Maxage-Exp.yaml`
    > Cache MUST cache the response if the Smaxage and Maxage and Expires

###Extensions
1. `case_rfc2616_extension-req-key=value.yaml`
    > cache MUST ignore cache-control key=value extension request

2. `case_rfc2616_extension-req-max-age-name.yaml`
    > cache MUST ignore max-age=5 in the name of key=value extension request

3. `case_rfc2616_extension-req-max-age-value.yaml`
    > cache MUST ignore max-age=5 in the value of key=value extension request

4. `case_rfc2616_extension-req-max-age-whole.yaml`
    > cache MUST ignore max-age=5 in the name of quoted extension request

5. `case_rfc2616_extension-req-max-agex.yaml`
    > cache MUST ignore max-agex extension request

6. `case_rfc2616_extension-req-xmax-age.yaml`
    > cache MUST ignore xmax-age extension request

7. `case_rfc2616_extension-resp-key=value.yaml`
    > cache MUST ignore cache-control key=value extension response

8. `case_rfc2616_extension-resp-max-age-name.yaml`
    > cache MUST ignore max-age=5 in the name of key=value extension response

9. `case_rfc2616_extension-resp-max-age-value.yaml`
    > cache MUST ignore max-age=5 in the value of key=value extension response

10. `case_rfc2616_extension-resp-max-age-whole.yaml`
    > cache MUST ignore max-age=5 in the name of quoted extension response

11. `case_rfc2616_extension-resp-max-agex.yaml`
    > cache MUST ignore max-agex extension response

12. `case_rfc2616_extension-resp-xmax-age.yaml`
    > cache MUST ignore xmax-age extension response

##Cache-Updates
###HEAD-Method
1. `case_rfc2616_CltHEADValidate-NewEntityHdr-Content-Length-200.yaml`
    > Client-control validation could use HEAD request with Cache-Control:(max-age=0) directive, when cache
	  go back to validate, and get a response "200 OK" with new Entity Header "Content-Length", the cache should regard
	  the cached object as old.

2. `case_rfc2616_CltHEADValidate-NewEntityHdr-Content-Length-304.yaml`
    > Client-control validation could use HEAD request with Cache-Control:(max-age=0) directive, when cache
	  go back to validate, and get a response "304 Not Modified" with new Entity Header "Content-Length", the cache should regard
	  the cached object as old.

3. `case_rfc2616_CltHEADValidate-NewEntityHdr-Content-MD5-200.yaml`
    > Client-control validation could use HEAD request with Cache-Control:(max-age=0) directive, when cache
	  go back to validate, and get a response "200 OK" with new Entity Header "Content-MD5", the cache should regard
	  the cached object as old.

4. `case_rfc2616_CltHEADValidate-NewEntityHdr-Content-MD5-304.yaml`
    > Client-control validation could use HEAD request with Cache-Control:(max-age=0) directive, when cache
	  go back to validate, and get a response "304 Not Modified" with new Entity Header "Content-MD5", the cache should regard
	  the cached object as old.

5. `case_rfc2616_CltHEADValidate-NewEntityHdr-ETag-200.yaml`
    > Client-control validation could use HEAD request with Cache-Control:(max-age=0) directive, when cache
	  go back to validate, and get a response "200 OK" with new Entity Header "Etag", the cache should regard
	  the cached object as old.

6. `case_rfc2616_CltHEADValidate-NewEntityHdr-ETag-304.yaml`
    > Client-control validation could use HEAD request with Cache-Control:(max-age=0) directive, when cache
	  go back to validate, and get a response "304 Not Modified" with new Entity Header "Etag", the cache should regard
	  the cached object as old.

7. `case_rfc2616_CltHEADValidate-NewEntityHdr-Last-Modified-200.yaml`
	> Client-control validation could use HEAD request with Cache-Control:(max-age=0) directive, when cache
	   go back to validate, and get a response "200 OK" with new Entity Header "Last-Modified", the cache should regard
	   the cached object as old.
8. `case_rfc2616_CltHEADValidate-NewEntityHdr-Last-Modified-304.yaml`
	> Client-control validation could use HEAD request with Cache-Control:(max-age=0) directive, when cache
	   go back to validate, and get a response "304 Not Modified" with new Entity Header "Last-Modified", the cache should regard
	   the cached object as old.

###Revalidation
1. `case_rfc2616_304-updates-Cache-Control-vals-old1-new1.yaml`
    > cache MUST update forwarded end-to-end headers after a 304 response with an updated Cache-Control header (Vary causing revalidation)

2. `case_rfc2616_304-updates-Cache-Control-vals-old1-new2.yaml`
    > cache MUST update forwarded end-to-end headers after a 304 response with 2 Cache-Control header(s) updating 1 orig-1-owjl header(s) (Vary causing revalidation)

3. `case_rfc2616_304-updates-Cache-Control-vals-old2-new1.yaml`
    > cache MUST update forwarded end-to-end headers after a 304 response with 1 Cache-Control header(s) updating 2 original header(s) (Vary causing revalidation)

4. `case_rfc2616_304-updates-Cache-Control-vals-old1-new2.yaml`
    > cache MUST update forwarded end-to-end headers after a 304 response with 2 Cache-Control header(s) updating 2 original header(s) (Vary causing revalidation)

5. `case_rfc2616_304-updates-Cache-Control-vals-old5-new5.yaml`
    > cache MUST update forwarded end-to-end headers after a 304 response with 5 Cache-Control header(s) updating 5 original header(s) (Vary causing revalidation)

6. `case_rfc2616_304-update-ContentLocation-with-vary.yaml`
    > cache MUST update forwarded end-to-end headers after a 304 response with an updated Date header (Vary causing revalidation)

7. `case_rfc2616_304-update-Date-with-vary.yaml`
    > cache MUST update forwarded end-to-end headers after a 304 response with an updated Date header (Vary causing revalidation)

8. `case_rfc2616_304-update-Expires-with-vary.yaml`
    > cache MUST update forwarded end-to-end headers after a 302 response with an updated Date header (Vary causing revalidation)

##Caching
###Authorization
1. `case_rfc2616_authorization-s-maxage=0-cacheRefresh.yaml`
    > a Authorization and  s-maxage=0 request make cache refresh

###Expires-Header
1. `case_rfc2616_expires-value-0blankQuoted.yaml`
    > expires value blank 0

2. `case_rfc2616_expires-value-0onlyQuoted.yaml`
    > expires equal zero english quoted

3. `case_rfc2616_expires-value-1DigitYear.yaml`
    >  expires value in 1digit year

4. `case_rfc2616_expires-value-empty.yaml`
    > expires value value empty

5. `case_rfc2616_expires-value-httpdlike.yaml`
    > expires value in apache httpd like date

6. `case_rfc2616_expires-value-longMonth.yaml`
    > expires value long month

7. `case_rfc2616_expires-value-negativeYear.yaml`
    > expires value in negative year

8. `case_rfc2616_expires-value-RFC850.yaml`
    > expires value in RFC850 format

9. `case_rfc2616_expires-value-RFC1123.yaml`
    > expires value in RFC1123 format

10. `case_rfc2616_expires-value-xxxMonth.yaml`
    > expires value xxx month

11. `case_rfc2616_expires-value-yesterdayString.yaml`
    > expires value yesterday string

###General-Caching
1. `case_rfc2616_bodyIncomplete-noCached.yaml`
    > bodysize less than content-length, dont't cache

2. `case_rfc2616_reqNoCache-cachedRssRefreshed.yaml`
    > DUT MUST use the more recent Date if the 2nd response Date is older than the 1st response Date in cache

3. `case_rfc2616_treat-query-URIs-stale-without-Expires.yaml`
    > cache MUST treat response to query URIs be stale if there is no Expires header in

4. `case_rfc2616_response-allowHead-multi-6Values.yaml`
    > cache MUST cache all values of a multi-valued Allow response header with 6 values

5. `case_rfc2616_response-allowHead-order-multi-6Values.yaml`
    > cache MUST preserve field-value order when caching multi-valued Allow response header with 6 values

6. `case_rfc2616_response-contentLanguageHead-multi-6Values.yaml`
    > cache MUST cache all values of a multi-valued Allow response header with 6 values

7. `case_rfc2616_response-contentLanguageHead-order-multi-6Values.yaml`
    > cache MUST preserve field-value order when caching multi-valued Content-Language response header with 6 values

8. `case_rfc2616_response-extHead-single-2LineSpace.yaml`
    > cache MUST cache single-valued 2-line spaced extension response header

9. `case_rfc2616_response-extHead-single-2LineTabbed.yaml`
    > cache MUST cache single-valued 2-line tabbed extension response header

10. `case_rfc2616_response-extHead-single-18LineTabbed.yaml`
    > cache MUST cache single-valued 18-line tabbed extension response header

11. `case_rfc2616_response-extHead-single-19LineSpace.yaml`
    > cache MUST cache single-valued 19-line spaced extension response header

12. `case_rfc2616_response-extHead-single-absentVal.yaml`
    > cache MUST cache single-valued extension response header with absent value

13. `case_rfc2616_response-extHead-single-longName.yaml`
    > cache MUST cache single-valued extension response header with long name

14. `case_rfc2616_response-extHead-single-longVal.yaml`
    > cache MUST cache single-valued extension response header with long value

15. `case_rfc2616_response-extHead-single-namedDot.yaml`
    > cache MUST cache single-valued extension response header named dot

16. `case_rfc2616_response-extHead-single-plainVal.yaml`
    > cache MUST cache single-valued extension response header with plain value

17. `case_rfc2616_response-pragmaHead-multi-7Values.yaml`
    > cache MUST cache all values of a multi-valued Pragma response header with 7 values

18. `case_rfc2616_response-pragmaHead-order-multi-7Values.yaml`
    > cache MUST preserve field-value order when caching multi-valued Pragma response header with 7 values

19. `case_rfc2616_response-serverHead-single-2LineSpace.yaml`
    > cache MUST cache single-valued 2-line spaced Server response header

20. `case_rfc2616_response-serverHead-single-2LineTabbed.yaml`
    > cache MUST cache single-valued 2-line tabbed Server response header

21. `case_rfc2616_response-serverHead-single-18LineTabbed.yaml`
    > cache MUST cache single-valued 18-line tabbed Server response header

22. `case_rfc2616_response-serverHead-single-19LineSpace.yaml`
    > cache MUST cache single-valued 19-line spaced Server response header

23. `case_rfc2616_response-serverHead-single-withComment.yaml`
    > cache MUST cache single-valued Server response header with a plain comment field

24. `case_rfc2616_response-serverHead-single-woutComment.yaml`
    > cache MUST cache single-valued Server response header without comment field

25. `case_rfc2616_response-single-woutDateHead.yaml`
    > cache MUST cache single-valued plain warning without Date response header

26. `case_rfc2616_response-viaHead-multi-6Values.yaml`
    > cache MUST cache all values of a multi-valued Via response header with 6 values

27. `case_rfc2616_response-viaHead-order-multi-6Values.yaml`
    > ache MUST preserve field-value order when caching multi-valued Via response header with 6 values

###Stale-Caching
1. `case_rfc2616_POST-stale-URLs-location.yaml`
    > POST method MUST stale cached URLs matching in responsed location entity

2. `case_rfc2616_POST-stale-URLs-in-Location-Content-Location.yaml`
    > POST method MUST stale all cached URLs in response  Location or Content-Location headers

3. `case_rfc2616_POST-stale-URLs-contained-in-content-location.yaml`
    > POST method MUST staled all cached URLs matching URLs in Content-Location

4. `case_rfc2616_POST-stale-URLs-relative-content-location.yaml`
    > POST method MUST invalidate all cached entries matching relative Content-Location URL

5. `case_rfc2616_POST-stale-POSTPURL-content-location.yaml`
    > POST method MUST invalidate all cached entries matching request or Content-Location URL

6. `case_rfc2616_POST-stale-POSTPURL-and-location.yaml`
    > POST method MUST invalidate all cached entries matching request or Location URL

7. `case_rfc2616_POST-not-stale-URLs-not-in-content-location.yaml`
    > POST method MUST NOT invalidate all cached URLs not included in response Content-Location entry

8. `case_rfc2616_POST-not-stale-URLs-not-in-Location-Content-Location.yaml`
    > POST method MUST NOT invalidate cached URL entries with the request URI not in response Location or Content-Location
 
9. `case_rfc2616_POST-not-stale-URLs-not-in-locatio.yaml`
    > POST method MUST NOT invalidate cached entries with request uri not in response Location entity

##Chunk
###Request-Chunked
1. `case_rfc2616_rqst-chunked-0B-block.yaml`
    > DUT MUST handle chunked request with 0-byte block

2. `case_rfc2616_rqst-chunked-0before-blksize.yaml`
    > DUT MUST handle chunked request with a zero before the block size

3. `case_rfc2616_rqst-chunked-1B-block.yaml`
    > DUT MUST handle chunked request with one 1-byte block

4. `case_rfc2616_rqst-chunked-2x100B-block.yaml`
    > DUT MUST handle chunked request with two 100-byte blocks

5. `case_rfc2616_rqst-chunked-3x0-in-lastblock.yaml`
    > DUT MUST handle chunked request with 3 zeros in the last chunk block

6. `case_rfc2616_rqst-chunked-incrct-bodylen.yaml`
    > DUT MUST handle chunked request with incorrect Content-Length header entity

###Response-Chunked
1. `case_rfc2616_response-chunked-0B-block-to10clt.yaml`
    > DUT MUST handle 0-length chunk block response to an HTTP/1.0 client

2. `case_rfc2616_response-chunked-1B-block-to10Clt.yaml`
    >  DUT MUST handle a chunked body with 1-byte block response to an HTTP/1.0 client

3. `case_rfc2616_response-chunked-100B-block-to10Clt.yaml`
    >  DUT MUST handle chunked body with one 100-byte block response to an HTTP/1.0 client

4. `case_rfc2616_response-chunked-2x100B-block-to10Clt.yaml`
    >  DUT MUST handle chunked body with two 100-byte blocks response to an HTTP/1.0 client

5. `case_rfc2616_response-chunked-1025x100B-block-to10Clt.yaml`
    >  DUT MUST handle chunked body with 1025 100-byte blocks response to an HTTP/1.0 client

6. `case_rfc2616_response-chunked-65535B-block-to10Clt.yaml`
    >  DUT MUST handle a chunked body with a 65535-byte block response to an HTTP/1.0 client

7. `case_rfc2616_response-chunked-65536B-block-to10Clt.yaml`
    >  DUT MUST handle a chunked body with a 65536-byte block response to an HTTP/1.0 client

8. `case_rfc2616_response-chunked-65537B-block-to10Clt.yaml`
    >  DUT MUST handle a chunked body with a 65537-byte block response to an HTTP/1.0 client

9. `case_rfc2616_response-chunked-errContentlen-to10Clt.yaml`
    >  DUT MUST handle chunked body with an incorrect Content-Length header response to an HTTP/1.0 client

10. `case_rfc2616_response-chunked-last-3x0-to10Clt.yaml`
    >  DUT MUST handle chunked body with 3 zeros in last chunk block response to an HTTP/1.0 client

11. `case_rfc2616_response-chunked-last-65x0-block-to10Clt.yaml`
    >  DUT MUST handle chunked body with 65 zeros in last chunked block response to an HTTP/1.0 client

12. `case_rfc2616_response-chunked-0leads-size-block-to10Clt.yaml`
    >  DUT MUST handle chunked body with a leading-zero block size in chunk blocks response to an HTTP/1.0 client

13. `case_rfc2616_response-chunked-0B-block-to11Clt.yaml`
    >  DUT MUST handle chunked body wiht 0-length block response sent to an HTTP/1.1 client

14. `case_rfc2616_response-chunked-1B-block-to11Clt.yaml`
    >  DUT MUST handle a chunked body with a 1-byte block response to an HTTP/1.1 client

15. `case_rfc2616_response-chunked-100B-block-to11Clt.yaml`
    >  DUT MUST handle chunked body with one 100-byte block responsed to an HTTP/1.1 client

16. `case_rfc2616_response-chunked-2x100B-block-to11Clt.yaml`
    >  DUT MUST handle chunked body with 2 100-byte blocks response to an HTTP/1.1 client

17. `case_rfc2616_response-chunked-1025x100B-block-to11Clt.yaml`
    >  DUT MUST handle a chunked body with 1025 100-byte blocks response to an HTTP/1.1 client

18. `case_rfc2616_response-chunked-65535B-block-to11Clt.yaml`
    >  DUT MUST handle a chunked body with a 65535-byte block response to an HTTP/1.1 client

19. `case_rfc2616_response-chunked-65536B-block-to11Clt.yaml`
    >  DUT MUST handle a chunked body with a 65536-byte block response to an HTTP/1.1 client

20. `case_rfc2616_response-chunked-65537B-block-to11Clt.yaml`
    >  DUT MUST handle a chunked body with a 65537-byte block response to an HTTP/1.1 client

21. `case_rfc2616_response-chunked-errContentlen-to11Clt.yaml`
    >  DUT MUST handle chunked body with an incorrect Content-Length header response to an HTTP/1.1 client

22. `case_rfc2616_response-chunked-last-3x0-to11Clt.yaml`
    >  DUT MUST handle chunked body with 3 zeros in last chunk block response to an HTTP/1.1 client

23. `case_rfc2616_response-chunked-last-65x0-block-to11Clt.yaml`
    >  DUT MUST handle chunked body with 65 zeros in last chunked block response to an HTTP/1.1 client

24. `case_rfc2616_response-chunked-0leads-size-block-to11Clt.yaml`
    >  DUT MUST handle chunked body with a leading-zero block size in chunk blocks response to an HTTP/1.1 client

25. `case_rfc2616_response-chunked-0B-body-extension-to10Clt.yaml`
    >  DUT MUST handle chunked body with 0-byte block and a chunk extention responsed to an HTTP/1.0 client

26. `case_rfc2616_response-chunked-quoted-16385-extval-to10Clt.yaml`
    >  DUT MUST handles chunked body with a 16385-byte quoted chunk-extention value response to an HTTP/1.0 client

27. `case_rfc2616_response-chunked-16385-extval-to10Clt.yaml`
    >  DUT MUST handle chunked body with a 16385-byte chunk-extetion value response to an HTTP/1.0 client

28. `case_rfc2616_response-chunked-named-extension-to10Clt.yaml`
    >  DUT MUST handle chunked body with a chunk-extension token response to an HTTP/1.0 client

29. `case_rfc2616_response-chunked-quoted-extension-to10Clt.yaml`
    >  DUT MUST handle chunked body with a quoted-string in a chunk extension response to an HTTP/1.0 client

30. `case_rfc2616_response-chunked-extension-spaced-to10Clt.yaml`
    >  DUT MUST handle chunked body with spaced chunk-extension response to an HTTP/1.0 client

31. `case_rfc2616_response-chunked-value-assigned-extension-to10Clt.yaml`
    >  DUT MUST handle chunked body with a valued chunk extension response to an HTTP/1.0 client

32. `case_rfc2616_response-chunked-0B-body-extension-to11Clt.yaml`
    >  DUT MUST handle chunked body with 0-byte block and a chunk extention responsed to an HTTP/1.1 client

33. `case_rfc2616_response-chunked-quoted-16385-extval-to11Clt.yaml`
    >  DUT MUST handles chunked body with a 16385-byte quoted chunk-ext-val response to an HTTP/1.1 client

34. `case_rfc2616_response-chunked-16385-extval-to11Clt.yaml`
    >  DUT MUST handle chunked body with a 16385-byte chunk-ext-val response to an HTTP/1.1 client

35. `case_rfc2616_response-chunked-named-extension-to11Clt.yaml`
    >  DUT MUST handle chunked body with a chunk-extension token response to an HTTP/1.1 client

36. `case_rfc2616_response-chunked-quoted-extension-to11Clt.yaml`
    >  DUT MUST handle chunked body with a quoted-string in a chunk extension response to an HTTP/1.1 client

37. `case_rfc2616_response-chunked-extension-spaced-to11Clt.yaml`
    >  DUT MUST handle chunked body with spaced chunk-extension response to an HTTP/1.1 client

38. `case_rfc2616_response-chunked-value-assigned-extension-to11Clt.yaml`
    >  DUT MUST handle chunked body with a valued chunk extension response to an HTTP/1.1 client

39. `case_rfc2616_chunked-1p1-cache-chunked.yaml`
    > DUT SHOULD cache chunked response with two 100Byte chunks if cache-control header is public

###Trailer
1. `case_rfc2616_request-chunked-0b-block-1-announced-trailer-woutTe.yaml`
    > DUT MUST handle chunked request with one 0-Byte chunk block and with 1 announced header in the trailer

2. `case_rfc2616_request-chunked-11b-block-1-announced-trailer.yaml`
    > DUT MUST handle chunked request with one 11-byte block and with 1 announced header in the trailer

3. `case_rfc2616_request-chunked-11b-block-1-surprise-trailer-woutTe.yaml`
    > DUT MUST handle chunked request with one 11-byte chunk block and with 1 surprise header in the trailer

4. `case_rfc2616_request-chunked-11b-block-17-announced-trailer.yaml`
    > DUT MUST handle chunked request with one 11-byte block and with 17 announced headers in the trailer

5. `case_rfc2616_request-chunked-11b-block-17-surprise-trailer.yaml`
    > DUT MUST handle chunked request with one 11-byte block and with 17 surprise headers in the trailer

6. `case_rfc2616_response-chunked-0-block-1-announced-trailer-woutTe-to10Clt.yaml`
    > DUT MUST handle chunked response with one 0-byte chunk block and with one announced header in the trailer response to an HTTP/1.0 client without sending TE trailers

7. `case_rfc2616_response-chunked-0b-block-1-announced-trailer-woutTe-to11Clt.yaml`
    > DUT MUST handle chunked body with one 0-byte block and with 1 announced header in the trailer response to an HTTP/1.1 client without TE: trailers

8. `case_rfc2616_response-chunked-11b-block-1-announced-trailer-withTe-to10Clt.yaml`
    > DUT MUST handle chunked response with one 11-byte chunk block and with 1 announced header in the trailer response to an HTTP/1.0 client with TE: trailers

9. `case_rfc2616_response-chunked-11b-block-1-announced-trailer-withTe-to11Clt.yaml`
    > DUT MUST handle chunked response with one 11-byte chunk block and with 1 announced header in the trailer response to an HTTP/1.1 client with TE: trailers

10. `case_rfc2616_response-chunked-11b-block-1-announced-trailer-woutTe-to10Clt.yaml`
     > DUT MUST handle chunked response with one 11-byte chunk block and with 1 announced header in the trailer response to an HTTP/1.0 client without TE: trailers

11. `case_rfc2616_response-chunked-11b-block-1-announced-trailer-woutTe-to11Clt.yaml`
     > DUT MUST handle chunked body with one 11-byte block and with 1 announced header in the trailer response to an HTTP/1.1 client without TE: trailers

12. `case_rfc2616_response-chunked-11b-block-1-surprise-trailer-withTe-to10Clt.yaml`
     > DUT MUST handle chunked response with one 11-byte chunk block and with 1 surprise header in the trailer response to an HTTP/1.0 client with TE: trailers

13. `case_rfc2616_response-chunked-11b-block-1-surprise-trailer-withTe-to11Clt.yaml`
     > DUT MUST handle chunked body with one 11-byte block and with 1 surprise header in the trailer response to an HTTP/1.1 client with TE: trailers

14. `case_rfc2616_response-chunked-11b-block-1-surprise-trailer-woutTe-to10Clt.yaml`
     > DUT MUST handle chunked body with one 11-byte body and with 1 surprise header in the trailer response to an HTTP/1.0 client without TE: trailers
 
15. `case_rfc2616_response-chunked-11b-block-1-surprise-trailer-woutTe-to11Clt.yaml`
     > DUT MUST handle chunked body with one 11-byte chunk block and with 1 surprise header in the trailer response to an HTTP/1.1 client without TE: trailers

16. `case_rfc2616_response-chunked-11b-block-17-announced-trailer-withTe-to10Clt.yaml`
     > DUT MUST handle chunked body with one 11-byte block and with 17 announced headers in the trailer sent to an HTTP/1.0 client with TE: trailers
 
17. `case_rfc2616_response-chunked-11b-block-17-announced-trailer-withTe-to11Clt.yaml`
     > DUT MUST handle chunked body with one 11-byte block and with 17 announced headers in the trailer response to an HTTP/1.1 client with TE: trailers

18. `case_rfc2616_response-chunked-11b-block-17-announced-trailer-woutTe-to10Clt.yaml`
     > DUT MUST handle chunked body with one 11-byte block and with 17 announced headers in the trailer response to an HTTP/1.0 client without TE: trailers

19. `case_rfc2616_response-chunked-11b-block-17-announced-trailer-woutTe-to11Clt.yaml`
     > DUT MUST handle chunked body with one 11-byte chunk and with 17 announced headers in the trailer response to an HTTP/1.1 client without TE: trailers

20. `case_rfc2616_response-chunked-11b-block-17-surprise-trailer-withTe-to10Clt.yaml`
     > DUT MUST handle chunked body with one 11-byte block and with 17 surprise headers in the trailer response to an HTTP/1.0 client with TE: trailers

21. `case_rfc2616_response-chunked-11b-block-17-surprise-trailer-withTe-to11Clt.yaml`
     > DUT MUST handle chunked body with one 11-byte body and with 17 surprise headers in the trailer response to an HTTP/1.1 client with TE: trailers

22. `case_rfc2616_response-chunked-11b-block-17-surprise-trailer-woutTe-to10Clt.yaml`
     > DUT MUST handle chunked body with one 11-byte block and with 17 surprise headers in the trailer response to an HTTP/1.0 client without TE: trailers

23. `case_rfc2616_response-chunked-11b-block-17-surprise-trailer-woutTe-to11Clt.yaml`
     > DUT MUST handle chunked body with one 11-byte block and with 17 surprise headers in the trailer response to an HTTP/1.1 client without TE: trailers

24. `case_rfc2616_rmRespTrailer-te-chunked.yaml`
     > DUT MUST remove trailer header entity if TE header is chunked

25. `case_rfc2616_rmRespTrailer-te-trailer.yaml`
     > DUT MUST remove the trailer header entity if TE header is trailer

26. `case_rfc2616_rmRespTrailer-te-xtrailers.yaml`
     > DUT MUST remove the trailer entity if TE header is xtrailers

##Conditional-Request
###if-Match
1. `case_rfc2616_ifMatch-reqUnsupportHost.yaml`
    > If-Match ignored unsupported Host(400 status)

2. `case_rfc2616_ifMatch-reqUnsupportExpect.yaml`
    > If-Match ignored unsupported Expect(417 status)

###If-None-Match
1. `case_rfc2616_mutiIfNoneMatch-noneIms.yaml`
    > MUST perform the requested have muti If-None-Match matches ETag but no If-Modified-Since
 
2. `case_rfc2616_ifNoneMatch-reqUnsupportExpect.yaml`
    > If-None-Match ignored unsupported Expect(417 status)

3. `case_rfc2616_ifNoneMatch-reqUnsupportHost.yaml`
    > If-None-Match ignored unsupported Host(400 status)

###If-Modified-Since
1. `case_rfc2616_304Modified-newTag.yaml` 
    > if-Modified-Since and a new ETag value ,refresh status and ETag

2. `case_rfc2616_rsp-without-lastModified-header.yaml`
    > When cache is expired, if response without Last-Modified header, request without If-Modified-Since header

###Multi-Conditional
1. `case_rfc2616_multiIf-timed-If-Range.yaml`
    > multiIf:If-None-Match-match,If-Modified-Since-match with If-Range-timed,cache refresh
2. `case_rfc2616_multiIf-tagged-If-Range.yaml`
    > multiIf:If-None-Match-match,If-Modified-Since-match with If-Range-tagged,cache refresh

##Content-Length
1. `case_rfc2616_POST-chunked_addCL_noTrailer`
    > proxy MUST add Content-Length header to request containing chunked-encoded body without trailer

##End-to-End-Headers

##Expect-Continue
1. `case_rfc2616_httpcode1XX-forward-MultiX-Header` 
    > proxy MUST forward multi response header x-headers when 101-status response(s) prior to a real response

##Gzip
1. `case_body_None.yaml`
    > DUT MUST handle content-length: 0  gzip response

2. `case_gzip_requestgzip.yaml`
    > verify DUT can handle gzip request and response support gzip

##Hop-By-Hop-Headers
1. `case_rfc2616_HopbyHop_NoCacheNoForward_Trailer_Response.yaml`
    > proxy MUST NOT forward hop-by-hop response header: Trailer

2. `case_rfc2616_HopbyHop_NoForward_Trailer_Req.yaml`
    > proxy MUST NOT forward hop-by-hop response header: Trailer

##Pragma-Headers
1. `case_rfc2616_pragma-req-withNocacheTokens.yaml`
    > proxy MUST pass through Pragma requests with no-cache tokens

2. `case_rfc2616_pragma-req-withParamQuotedValue.yaml`
    > proxy MUST pass through Pragma requests with param=quoted-value tokens

3. `case_rfc2616_pragma-req-withParamValue.yaml`
    > proxy MUST pass through Pragma requests with param=value tokens

4. `case_rfc2616_pragma-req-withSeveralTokens.yaml`
    > proxy MUST pass through Pragma requests with several tokens

5. `case_rfc2616_pragma-resp-withNocacheTokens.yaml`
    > proxy MUST pass through Pragma responses with no-cache tokens

6. `case_rfc2616_pragma-resp-withParamQuotedValue.yaml`
    > proxy MUST pass through Pragma responses with param=quoted-value tokens

7. `case_rfc2616_pragma-resp-withParamValue.yaml`
    > proxy MUST pass through Pragma responses with param=value tokens

8. `case_rfc2616_pragma-resp-withSeveralTokens.yaml`
    > pragma response with several tokens ,can be through

##Range 
1. `case_rfc2616_range-interval-invalid.yaml`
    > server MUST ignore the range header entity that includes syntactically invalid range

2. `case_rfc2616_spaced-invalid-Range.yaml`
    > server MUST ignore the Range header that includes a syntactically invalid spaced range

3. `case_rfc2616_multiRanges-1-valid-2-invalid.yaml`
    > Server MUST ignore the range header entity that includes two range intervals and the first range is valid, the second is invalid

4. `case_rfc2616_multiRange-1-3-valid-2-invalid.yaml`
    > server MUST ignore the range header entity that includes three range intervals: the first and third is valid and the second is invalid

5. `case_rfc2616_upper-bound-negative.yaml`
    > server MUST ignore the range header entity that includes a negative upper bound range interval

6. `case_rfc2616_octal-start-range.yaml`
    >  server MUST ignore the range header entity that includes range start with an octal number

7. `case_rfc2616_twoRanges-2nd-infinite.yaml`
    > server MUST ignore the range header entity that includes two ranges: the last without upper bound

8. `case_rfc2616_twoinvalidRanges-1st-no-upper-bound.yaml`
    > server MUST ignore the range header entity that includes two invalid range intervals and the first range without upper bound
         
##Status-Codes
###304-Code
1. `case_rfc2616_If-None-Match-Vary-strongMatch.yaml`
    >If-None-Match strong match with Vary header

2. `case_rfc2616_If-None-Match-weakMatch.yaml`
    >If-None-Match weak match 

3. `case_rfc2616_If-None-Match-NoVary-strongMatch.yaml`
    >If-None-Match strong match without Vary header

###Uncacheable-Codes
1. `case_rfc2616_NoCache-IfNotForce-SC-302.yaml`
    > the status code 302 MUST NOT be cached if not "explicitly force to cache"

2. `case_rfc2616_NoCache-IfNotForce-SC-306.yaml`
    > the status code 306 MUST NOT be cached if not "explicitly force to cache"

3. `case_rfc2616_NoCache-IfNotForce-SC-307.yaml`
    > the status code 307 MUST NOT be cached if not "explicitly force to cache"

4. `case_rfc2616_NoCache-IfNotForce-SC-409.yaml`
    > the status code 409 MUST NOT be cached if not "explicitly force to cache"

5. `case_rfc2616_NoCache-IfNotForce-SC-500.yaml`
    > the status code 500 MUST NOT be cached if not "explicitly force to cache"

6. `case_rfc2616_NoCache-UnKnowSC-290.yaml`
    > HTTP Protocol Unknow status code MUST NOT be cached: 290

7. `case_rfc2616_NoCache-UnKnowSC-390.yaml`
    > HTTP Protocol Unknow status code MUST NOT be cached: 390

8. `case_rfc2616_NoCache-UnKnowSC-490.yaml`
    > HTTP Protocol Unknow status code MUST NOT be cached: 490

9. `case_rfc2616_NoCache-UnKnowSC-590.yaml`
    > HTTP Protocol Unknow status code MUST NOT be cached: 590

##Uncacheable-Methods
1. `case_rfc2616_DELETE-request-notcache.yaml`
    > cache MUST NOT cache response to DELETE request

2. `case_rfc2616_OPTIONS-request-notcache.yaml`
    > cache MUST NOT cache response to OPTIONS request

3. `case_rfc2616_POST-request-notcache.yaml`
    > cache MUST NOT cache response to POST request

4. `case_rfc2616_PUT-request-notcache.yaml`
    > cache MUST NOT cache response to PUT request

5. `case_rfc2616_TRACE-request-notcache.yaml`
    > cache MUST NOT cache response to TRACE request


##Vary
1. `case_varyx1_MultiCopy_MisMathwith-X-Header.yaml`
    > cache MUST revalidate when the url has multi copy based on Header 'Vary', if the Vary defined header is diff

2. `case_varyx2_MultiCopy_MisMathwith-X-Vary2.yaml`
    > Cache Must revalidate object with 2 Vary header, when one header match and second is mismatch

3. `case_rfc2616_vary_Mismatch-add-extra-2ndReq.yaml`
    > cache MUST revalidate when the 2nd request add one extra vary header value

4. `case_rfc2616_vary_Mismatch-miss-one-2ndReq.yaml``
    > cache MUST revalidate if the 2nd request miss one vary header value

5. `case_rfc2616_vary_Mismatch-asterisk-vary.yaml``
    > cache MUST revalidate when "*" Vary header was used in 2nd request


##swift
1. `case_ContentLengthNone_NoChunk_ConnectionClose.yaml`
    > cache MUST handle a response without Content-Length and Transfer-Encoding header, Here, If the connection is close, read util the connection close, else return 502 or other httpcode to tell the server error

2. `case_ContentLengthNone_NoChunk_ConnectionKA.yaml`
    > Server response without Content-length, without Tranfser-Encoding But with Connection:keep-alive

##ts
1. `case_rfc2616_INM_range.yaml`
    > DUT MUST handle range request with E-tag header

2. `check_content_range.yaml`
    > cache should able to handle stale response 304 with Content-Range
