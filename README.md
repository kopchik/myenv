myenv
=====


It's like /usr/bin/env, but supports arguments passing to
the script. E.g:

~~~~
cd /tmp  # the right place for temporary files
script="./test.file"
cat << EOF > $script
#!/usr/bin/myenv -- python3 -O

# python -O should set __debug__ to False
assert __debug__ == False
print("test passed")
EOF

chmod +x $script
$script
cd -  # return to the original dir
~~~~

The '--' is mandatory because -O would treated as an argument
for "myenv", not for "python3". The output would be:

~~~
test passed
~~~

A ``normal'' **/usr/bin/env** would fail with this error:
~~~~
$./test.file
/usr/bin/env: python3 -O: No such file or directory
# or this one
/usr/bin/env: unrecognized option '-- python3 -O'
~~~~

This is because env does not parse arguments.