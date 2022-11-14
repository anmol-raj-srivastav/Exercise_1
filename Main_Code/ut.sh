# cat src/data/capk.yaml | grep image: -A1
# cat src/data/final.yaml | grep imagePullPolicy: | wc -l
# cat src/data/capk.yaml | grep imagePullPolicy: | wc -l
function ut1() {
    echo UT1 - Number of image Tag
    ORGINAL_IMAGE_TAG=`cat capk.yaml | grep image: | wc -l`
    FINAL_IMAGE_TAG=`cat final10.yaml | grep image: | wc -l`
    echo $ORGINAL_IMAGE_TAG
    echo $FINAL_IMAGE_TAG
    if [ $ORGINAL_IMAGE_TAG == $FINAL_IMAGE_TAG ]; then
        echo "UT1 Passed"
    else
        echo "UT1 Failed"
    fi
}
function ut2() {
    echo UT2 - Number of imagePullPolicy Tag
    ORGINAL_IPP_TAG=`cat /Users/anmolrajsrivastav/exercise1_yaml/unit_cases/case2.yaml | grep imagePullPolicy: | wc -l`
    FINAL_IPP_TAG=`cat /Users/anmolrajsrivastav/exercise1_yaml/unit_cases/case2_output.yaml | grep imagePullPolicy: | wc -l`
    CHANGED=$(expr $ORGINAL_IPP_TAG - $FINAL_IPP_TAG)
    
    if [ $CHANGED != 0 ]; then
        echo "UT2 - Changed/Added $CHANGED imagePullPolicy Tag"
    else
        echo "UT2 - No additional imagePullPolicy Tag"
    fi
}

function ut3() {
    echo UT2 - Number of imagePullPolicy Tag
    ORGINAL_IPP_TAG=`cat /Users/anmolrajsrivastav/exercise1_yaml/unit_cases/case3.yaml | grep imagePullPolicy: | wc -l`
    FINAL_IPP_TAG=`cat /Users/anmolrajsrivastav/exercise1_yaml/unit_cases/case3_output.yaml | grep imagePullPolicy: | wc -l`
    CHANGED=$(expr $ORGINAL_IPP_TAG - $FINAL_IPP_TAG)
    
    if [ $CHANGED != 0 ]; then
        echo "UT2 - Changed/Added $CHANGED imagePullPolicy Tag"
    else
        echo "UT2 - No additional imagePullPolicy Tag"
    fi
}

function ut4() {
    echo UT2 - Number of imagePullPolicy Tag
    ORGINAL_IPP_TAG=`cat /Users/anmolrajsrivastav/exercise1_yaml/unit_cases/case4.yaml | grep imagePullPolicy: | wc -l`
    FINAL_IPP_TAG=`cat /Users/anmolrajsrivastav/exercise1_yaml/unit_cases/case4_output.yaml | grep imagePullPolicy: | wc -l`
    CHANGED=$(expr $ORGINAL_IPP_TAG - $FINAL_IPP_TAG)
    
    if [ $CHANGED != 0 ]; then
        echo "UT2 - Changed/Added $CHANGED imagePullPolicy Tag"
    else
        echo "UT2 - No additional imagePullPolicy Tag"
    fi
}
function ut5() {
    echo UT2 - Number of imagePullPolicy Tag
    ORGINAL_IPP_TAG=`cat /Users/anmolrajsrivastav/exercise1_yaml/unit_cases/case1.yaml | grep imagePullPolicy: | wc -l`
    FINAL_IPP_TAG=`cat /Users/anmolrajsrivastav/exercise1_yaml/unit_cases/case1_output.yaml | grep imagePullPolicy: | wc -l`
    CHANGED=$(expr $ORGINAL_IPP_TAG - $FINAL_IPP_TAG)
    
    if [ $CHANGED != 0 ]; then
        echo "UT2 - Changed/Added $CHANGED imagePullPolicy Tag"
    else
        echo "UT2 - No additional imagePullPolicy Tag"
    fi
}

ut1
echo \\n
ut2
echo \\n
ut3
echo \\n
ut4
echo \\n
ut5