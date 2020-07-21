**Challenge:** panda.zip

Knowing that the password is a PIN number, we can perform a brute force attack.

Discovering the zip password: `./brute-force.sh`

Comparing the files: `diff <(xxd panda.jpg) <(xxd panda1.jpg) | grep '>' | cut -d ' ' -f12`

**Flag:** csictf{kung_fu_p4nd4}
