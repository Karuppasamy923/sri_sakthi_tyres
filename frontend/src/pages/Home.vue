<template>
  <div class="m-[5%]">
    <div class="fixed top-0 left-0 right-0 bg-white z-10 shadow-md py-4 px-6 flex items-center justify-between">
      <img src="https://www.digitire.com/cdn/shop/files/HORIZONTAL_ROXA_1_1200x1200.png?v=1652820934" alt="Company Logo" class="ml-[40px] h-[120px] w-auto">
      <div v-if="Auth" class="flex flex-col space-y-1 items-center mr-[50px]"> 
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/User_icon_2.svg/1200px-User_icon_2.svg.png" alt="user" class="h-[60px] w-auto">
        <h1 class="text-[20px] font-bold mb-6">Welcome User 1</h1>
      </div>
    </div>
    <div>

      <div v-if="!selectImg" class="flex justify-center mt-[300px]"> 
        <div class="flex flex-row space-x-8"> 
          <img class="w-237 h-188" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0-FVVaYSFbTMXiC6bUW2O_Vzx0OyauBu_RwRlfQ7iIU5aMvWJ86dpdfvGL7eYThBSkQ0&usqp=CAU" alt="person-1" @click="handleImgSelection"/>
          <img class="w-237 h-188" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0-FVVaYSFbTMXiC6bUW2O_Vzx0OyauBu_RwRlfQ7iIU5aMvWJ86dpdfvGL7eYThBSkQ0&usqp=CAU" alt="person-2" @click="handleImgSelection"/>
          <img class="w-237 h-188" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0-FVVaYSFbTMXiC6bUW2O_Vzx0OyauBu_RwRlfQ7iIU5aMvWJ86dpdfvGL7eYThBSkQ0&usqp=CAU" alt="person-3" @click="handleImgSelection"/>
          <img class="w-237 h-188" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0-FVVaYSFbTMXiC6bUW2O_Vzx0OyauBu_RwRlfQ7iIU5aMvWJ86dpdfvGL7eYThBSkQ0&usqp=CAU" alt="person-4" @click="handleImgSelection"/>
        </div>
      </div>
      <div v-if="selectImg && !Auth" class="flex flex-col space-y-3 justify-center mt-[300px] items-center "> 
        <div v-if="incorrect" class="flex items-center p-4 mb-4 text-lg text-red-800 border border-red-300 rounded-lg bg-red-50 dark:bg-white-800 dark:text-red-800 dark:border-red-900" role="alert">
          <svg class="flex-shrink-0 inline w-5 h-5 me-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
            <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z"/>
          </svg>
          <span class="sr-only">Info</span>&nbsp;
          <div>
            <span class="font-medium">Danger alert!</span> Change a few things up and try submitting again.
          </div>
        </div>
        <div> 
          <FeatherIcon name="arrow-left" class="w-10 h-10 absolute top-[15%] right-[93%] cursor-pointer" @click="selectImg=false"/>
        </div>
        <div class="flex flex-col space-y-7 justify-center items-center p-[60px] rounded-lg" style="box-shadow: 5px 5px 10px rgba(1, 1, 0.5, 0.5); background: linear-gradient(135deg, #7469B6, #AD88C6, #E1AFD1);">
          <div class="mb-4" style="width: 237.48px; height: 227.17px;"> 
              <img style="width: 100%; height: 100%; object-fit: contain;" :src="data.selectedImgSrc" :alt="data.selectedAlt"/>
          </div>
          <div class="mb-4">  
              <h1 class="text-center text-2xl font-semibold" style="color: #333;">User-1</h1>
          </div>
          <div class="mb-4"> 
              <h1 class="text-xl font-semibold" style="color: #333;">Enter your 4 Digit Pin</h1>
          </div>
          <div class="flex flex-row space-x-8"> 
              <input class="w-16 h-16 text-center border-2 border-black-500 bg-gray-200 rounded-lg" type="password" v-model="pin1" maxlength="1" @input="focusNext($event, 1)" style="color: #333;">
              <input class="w-16 h-16 text-center border-2 border-black-500 bg-gray-200 rounded-lg" type="password" v-model="pin2" maxlength="1" @input="focusNext($event, 2)" style="color: #333;">
              <input class="w-16 h-16 text-center border-2 border-black-500 bg-gray-200 rounded-lg" type="password" v-model="pin3" maxlength="1" @input="focusNext($event, 3)" style="color: #333;">
              <input class="w-16 h-16 text-center border-2 border-black-500 bg-gray-200 rounded-lg" type="password" v-model="pin4" maxlength="1" @input="focusNext($event, 4)" style="color: #333;">
          </div>
        </div>
      </div>
      <!-- main page -->
      <div v-if="currentstep == 0 && Auth"> 
          <div class="pt-24"> 
            <div v-if="currentstep == 0">
              <div class="flex justify-center m-5">
              <input type="text" class="w-[338px] h-[52px] rounded-sm border-solid border border-black" v-model="searchQuery">
              <button class="bg-blue-500 w-[150px] text-white font-bold text-base p-4 rounded-lg ml-3"
               @click="Search">Search</button>
            </div>
            <div class="grid grid-cols-2 gap-4">
          <Card>
          <div>
            <h4 class="text-[20px] font-bold">Vehicle Details</h4>
            <hr class="dark-hr">
            <div class="grid grid-cols-2 gap-4">
              <div>
                <p class="mt-3">Vehicle Number&emsp;&nbsp;&nbsp;: TN 47 SL 7784</p>
                <p class="mt-3">Vehicle Brand&emsp;: Tata</p>
                <p class="mt-3">Fuel Type&emsp;&emsp;&nbsp;&nbsp;&nbsp;: Diesel</p>
                <p class="mt-3">Tyre Change (kms)&nbsp;:25,000 kms</p>
              </div>
              <div>
                <p class="mt-3">Vehicle Model&emsp;: Indica Vista</p>
                <p class="mt-3">Chassis No&emsp;&nbsp;&nbsp;&emsp;: MAT611261APK75576</p>
                <p class="mt-3">Odometer Value&emsp;: Indica Vista</p>
                <p class="mt-3">Alignment (kms)&emsp;: 10,000 kms</p>
              </div>
            </div>
            <div class="mt-[70px] flex flex-row space-x-9">
              <button class="bg-blue-500 w-[150px] text-white font-bold  p-4 rounded-lg ml-3" @click="addVehicle">
                Add Vehicle
              </button>
              <button class="bg-blue-500 w-[150px] text-white font-bold  p-4 rounded-lg ml-3"
                @click="modifyVehicle">Modify</button>
            </div>
          </div>
        </Card>
        <Card>
          <div>
            <h4 class="text-[20px] font-bold">Customer Details</h4>
            <hr class="dark-hr">
            <div class="grid grid-cols-2 gap-4">
              <div>
                <p class="mt-3">Owner Name&emsp;&emsp;: Arumugaraja R <br>
                  <input type="checkbox" class="bg-gray-300 rounded-sm">&nbsp;&nbsp;WhatsApp
                  <span class="ml-5">
                    <input type="checkbox" class="bg-gray-300 rounded-sm">&nbsp;&nbsp;Call
                  </span>
                </p>
                <p class="mt-3">Driver Name&emsp;&emsp;: Krishna <br>
                  <input type="checkbox" class="bg-gray-300 rounded-sm">&nbsp;&nbsp;WhatsApp
                  <span class="ml-5">
                    <input type="checkbox" class="bg-gray-300 rounded-sm">&nbsp;&nbsp;Call
                  </span>
                </p>
                <p class="mt-3">Contact Person&emsp;&emsp;: Harish Krishna <br>
                  <input type="checkbox" class="bg-gray-300 rounded-sm">&nbsp;&nbsp;WhatsApp
                  <span class="ml-5">
                    <input type="checkbox" class="bg-gray-300 rounded-sm">&nbsp;&nbsp;Call
                  </span>
                </p>
              </div>
              <div>
                <p class="mt-3">Customer Mobile No: 9876543210 <br>
                  <input type="checkbox" class="bg-gray-300 rounded-sm">&nbsp;&nbsp;Email
                </p>
                <p class="mt-3">Driver Mobile No: 9876543210 <br>
                  <input type="checkbox" class="bg-gray-300 rounded-sm">&nbsp;&nbsp;Email
                </p>
                <p class="mt-3">Contact Person No: 9876543210 <br>
                  <input type="checkbox" class="bg-gray-300 rounded-sm">&nbsp;&nbsp;Email
                </p>
              </div>
            </div>
            <div class="float-right mt-[20px] flex flex-row space-x-9">
              <button class="bg-blue-500 w-[150px] text-white font-bold  p-4 rounded-lg ml-3" @click="addCustomer">
                Add Customer
              </button>
              <button class="bg-blue-500 w-[150px] text-white font-bold  p-4 rounded-lg ml-3"
                @click="modifyCustomer">Modify</button>
            </div>
          </div>
        </Card>
      </div>

      <div v-if="showNewVehicle"
        class="fixed inset-0 overflow-hidden bg-black bg-opacity-50 flex justify-end items-center">
        <div class="fixed inset-0" @click="addVehicle"></div>
        <div class="max-w-sm w-full bg-white shadow-xl h-full overflow-y-auto relative">
          <button class="absolute to text-black pt-5 font-bold p-2 right-2  px-2 py-1 rounded" @click="addVehicle">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
              stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
          <div class="p-8 mt-[140px]  ">
            <h2 class="text-2xl font-semibold mb-4 ">Vehicle Details</h2>
            <hr class="dark-hr">
            <p class="m-2">Vehicle Number <br>
              <input type="text" class="w-[280px] h-[52px] bg-gray-300 mt-1 rounded-sm border-solid border border-black" v-model="vehicleData.vehicleNumber"
                placeholder="Enter your Vehicle Number">
            </p>
            <p class="m-2">Vehicle Brand <br>
              <input type="text" class="w-[280px] h-[52px] bg-gray-300 mt-1 rounded-sm border-solid border border-black" v-model="vehicleData.vehicleBrand"
                placeholder="Enter Vehicle Brand">
            </p>
            <p class="m-2">Vehicle Model <br>
              <input type="text" class="w-[280px] h-[52px] bg-gray-300 mt-1 rounded-sm border-solid border border-black" v-model="vehicleData.vehicleModel"
                placeholder="Enter Vehicle Model">
            </p>
            <p class="m-2">Chassis No <br>
              <input type="text" class="w-[280px] h-[52px] bg-gray-300 mt-1 rounded-sm border-solid border border-black" v-model="vehicleData.chassisNo"
                placeholder="Enter Chassis No">
            </p>
            <p class="m-2">Fuel Type <br>
              <input type="text" class="w-[280px] h-[52px] bg-gray-300 mt-1 rounded-sm border-solid border border-black" v-model="vehicleData.fuelType"
                placeholder="Enter Fuel Type">
            </p>
            <p class="m-2">Odometer Value <br>
              <input type="text" class="w-[280px] h-[52px] bg-gray-300 mt-1 rounded-sm border-solid border border-black" v-model="vehicleData.odometerValue"
                placeholder="Enter Odometer Value">
            </p>
            <p class="m-2">Tyre Change (kms) <br>
              <input type="text" class="w-[280px] h-[52px] bg-gray-300 mt-1 rounded-sm border-solid border border-black" v-model="vehicleData.tyreChange"
                placeholder="Enter Tyre Change">
            </p>
            <p class="m-2">Alignment (kms) <br>
              <input type="text" class="w-[280px] h-[52px] bg-gray-300 mt-1 rounded-sm border-solid border border-black" v-model="vehicleData.alignment"
                placeholder="Enter Alignment">
            </p>
            <div class="m-3 mt-4 flex flex-row space-x-[70px]">
              <button class="bg-green-500 w-[100px] text-white font-bold 0 p-2 rounded" @click="addVehicleData">Add</button>
              <button class="bg-red-500 w-[100px] text-white font-bold ml-3 p-2 rounded" @click="clearVehicleData">Clear</button>
            </div>
          </div>
        </div>
      </div>

      <div v-if="showModifyVehicle"
        class="fixed inset-0 overflow-hidden bg-black bg-opacity-50 flex justify-end items-center">
        <div class="fixed inset-0" @click="modifyVehicle"></div>
        <div class="max-w-sm w-full bg-white shadow-xl h-full overflow-y-auto relative">
          <button class="absolute to text-black pt-5 font-bold p-2 right-2 px-2 py-1 rounded" @click="modifyVehicle">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
              stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
          <div class="p-8 mt-[140px]">
            <h2 class="text-2xl font-semibold mb-4">Vehicle Details</h2>
            <hr class="dark-hr">
            <p class="m-2">Vehicle Number <br>
              <input type="text" class="w-[280px] h-[52px] bg-gray-300 mt-1 rounded-sm border-solid border border-black" v-model="vehicleDetails.vehicleNumber"
                placeholder="Enter your Vehicle Number">
            </p>
            <p class="m-2">Vehicle Brand <br>
              <input type="text" class="w-[280px] h-[52px] bg-gray-300 mt-1 rounded-sm border-solid border border-black" v-model="vehicleDetails.vehicleBrand"
                placeholder="Enter Vehicle Brand">
            </p>
            <p class="m-2">Vehicle Model <br>
              <input type="text" class="w-[280px] h-[52px] bg-gray-300 mt-1 rounded-sm border-solid border border-black" v-model="vehicleDetails.vehicleModel"
                placeholder="Enter Vehicle Model">
            </p>
            <p class="m-2">Chassis No <br>
              <input type="text" class="w-[280px] h-[52px] bg-gray-300 mt-1 rounded-sm border-solid border border-black" v-model="vehicleDetails.chassisNo"
                placeholder="Enter Chassis No">
            </p>
            <p class="m-2">Fuel Type <br>
              <input type="text" class="w-[280px] h-[52px] bg-gray-300 mt-1 rounded-sm border-solid border border-black" v-model="vehicleDetails.fuelType"
                placeholder="Enter Fuel Type">
            </p>
            <p class="m-2">Odometer Value <br>
              <input type="text" class="w-[280px] h-[52px] bg-gray-300 mt-1 rounded-sm border-solid border border-black" v-model="vehicleDetails.odometerValue"
                placeholder="Enter Odometer Value">
            </p>
            <p class="m-2">Tyre Change (kms) <br>
              <input type="text" class="w-[280px] h-[52px] bg-gray-300 mt-1 rounded-sm border-solid border border-black" v-model="vehicleDetails.tyreChange"
                placeholder="Enter Tyre Change">
            </p>
            <p class="m-2">Alignment (kms) <br>
              <input type="text" class="w-[280px] h-[52px] bg-gray-300 mt-1 rounded-sm border-solid border border-black" v-model="vehicleDetails.alignment"
                placeholder="Enter Alignment">
            </p>
            <div class="m-3 mt-4 flex flex-row space-x-[70px]">
              <button class="bg-green-500 w-[100px] text-white font-bold 0 p-2 rounded" @click="addModifiedData">Add</button>
              <button class="bg-red-500 w-[100px] text-white font-bold ml-3 p-2 rounded"
                @click="clearModifiedVehicleData">Clear</button>
            </div>
          </div>
        </div>
      </div>

      <div v-if="showNewCustomer"
        class="fixed inset-0 overflow-hidden bg-black bg-opacity-50 flex justify-end items-center pb-9">
        <div class="fixed inset-0" @click="addCustomer"></div>
        <div class="max-w-sm w-full bg-white shadow-xl h-full overflow-y-auto relative">
          <button class="absolute to text-gray pt-5 font-bold p-2 right-2 px-2 py-1 rounded" @click="addCustomer">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
              stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
          <div class="p-8 mt-[150px]">
            <h2 class="text-2xl font-semibold mb-4">Customer Details</h2>
            <hr class="dark-hr">
            <p class="m-2">Owner Name <br>
              <input type="text" v-model="customerData.ownerName" class="w-[280px] h-[52px] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                placeholder="Enter your Owner Name">
            </p>
            <p class="m-2">Owner Mobile No <br>
              <input type="text" v-model="customerData.ownerMobile" class="w-[280px] h-[52px] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                placeholder="Enter Owner Mobile No.">
            </p>
            <!-- <hr class="dark-hr"> -->
            <div v-for="(employee, index) in employees" :key="index" class="mt-2">
              <hr class="dark-hr m-4">
              <p class="m-2">Employee Name
                <button class="bg-blue-500 w-[100px] text-white font-bold  text-base p-4 rounded-lg mb-1 float-right"
                  @click="removeEmployee1(index)">Remove</button> <br>
                <br>
                <input type="text" v-model="employee.name" class="w-[280px] h-[52px] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                  placeholder="Enter your Name">
              </p>
              <p class="m-2">Employee Type<br>
                <select v-model="employee.type" class="w-[280px] h-[52px] bg-gray-300 mt-1 rounded-sm border-solid border border-black">
                  <option value="Driver">Driver</option>
                  <option value="Contact Person">Contact Person</option>
                </select>
              </p>
              <p class="m-2">Phone <br>
                <input type="text" v-model="employee.phone" class="w-[280px] h-[52px] bg-gray-300 mt-1 rounded-sm border-solid border border-black">
              </p>
            </div>
            <div>
              <button class="bg-blue-500 w-[100px] text-white font-bold  text-base p-4 rounded-lg mb-1 float-right"
                @click="moreEmployee">Add
              </button><br>
            </div>
            <div class="m-3 mt-[40px] flex flex-row space-x-[70px]">
              <button class="bg-green-500 w-[100px]  text-white font-bold 0 text-base p-4 rounded-lg ml-3"
                @click="addCustomerData">Save</button>
              <button class="bg-red-500 w-[100px]  text-white font-bold text-base p-4 rounded-lg ml-3"
                @click="removeCustomerData">Clear</button>
            </div>
          </div>
        </div>
      </div>

      <div v-if="showModifyCustomer"
        class="fixed inset-0 overflow-hidden bg-black bg-opacity-50 flex justify-end items-center pb-5">
        <div class="fixed inset-0" @click="modifyCustomer"></div>
        <div class="max-w-sm w-full bg-white shadow-xl h-full overflow-y-auto relative">
          <button class="absolute to text-black pt-5 font-bold right-2 px-2 py-1 rounded" @click="modifyCustomer">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
              stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
          <div class="p-8 mt-[140px]">
            <h2 class="text-2xl font-semibold mb-4">Customer Details</h2>
            <hr class="dark-hr">
            <p class="m-2">Owner Name <br>
              <input type="text" v-model="employeesDetails.ownerName" class="w-[280px] h-[52px] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                placeholder="Enter your Owner Name">
            </p>
            <p class="m-2">Owner Mobile No <br>
              <input type="text" v-model="employeesDetails.ownerMobile" class="w-[280px] h-[52px] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                placeholder="Enter Owner Mobile No.">
            </p>
            <div v-for="(employee, index) in employeesDetails.employees" :key="index" class="mt-2">
              <hr class="dark-hr m-4">
              <p class="m-3">Employee Name
                <button class="bg-blue-500 w-[100px] text-white font-bold  text-base p-4 rounded-lg mb-1 float-right"
                  @click="removeEmployee2(index)">Remove</button> <br>
                <input type="text" v-model="employee.name" class="w-[280px] h-[52px] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                  placeholder="Enter your Name">
              </p>
              <p class="m-2">Employee Type<br>
                <select v-model="employee.type" class="w-[280px] h-[52px] bg-gray-300 mt-1 rounded-sm border-solid border border-black">
                  <option value="Driver">Driver</option>
                  <option value="Contact Person">Contact Person</option>
                </select>
              </p>
              <p class="m-2">Phone <br>
                <input type="text" v-model="employee.phone" class="w-[280px] h-[52px] bg-gray-300 mt-1 rounded-sm border-solid border border-black">
              </p>
            </div>
            <div>
              <button class="bg-blue-500 w-[100px] text-white font-bold  text-base p-4 rounded-lg mb-1 float-right"
                @click="modifiedMoreEmployee">Add
              </button><br>
            </div>
            <div class="m-3 mt-[40px] flex flex-row space-x-[70px]">
              <button class="bg-green-500 w-[100px]  text-white font-bold 0 text-base p-4 rounded-lg ml-3"
                @click="addModifiedCustomerData">Save</button>
              <button class="bg-red-500 w-[100px]  text-white font-bold text-base p-4 rounded-lg ml-3"
                @click="removeModifiedCustomerData">Clear</button>
            </div>
          </div>
        </div>
      </div>
      </div>
          </div>
      </div>
      <!-- 5 point check up  -->
      <div v-if="currentstep == 1"> 
        <div class="pt-24"> 
          <div class="flex flex-row">
            <h1 class="text-[20px] font-bold mt-5">5 Points Checkup</h1> 
            <button class="ml-[1410px] mb-4 text-[20px]  text-white w-[150px] h-[50px] bg-blue-500 rounded-lg" @click="addTyre">Add</button>
          </div>
          <hr class="mt-2 " :style="{ borderWidth: '2px', borderColor: 'gray' }"> 
          <div class="flex flex-col space-y-5 mt-4  p-4 bg-gray-200 rounded-lg shadow-md transition-shadow duration-300 hover:shadow-lg" v-for="(tyreData, index) in tyreDatas" :key="index"> 
            <div class="flex flex-row space-x-[70px]"> 
              <div class="flex flex-col space-y-1 ml-4">
                <label class="mt-2" :for="'tyre'+index">Tyre</label>
                <select class="w-[338px] h-[52px] rounded-sm" v-model="tyreData.tyre" :id="'type'+index" style="border: 1px solid black;" @change="updateTyreData(index)">
                  <option value="" selected disabled hidden>Please select...</option>
                  <option value="Front-Left">Front-Left</option>
                  <option value="Front-Right">Front-Right</option>
                  <option value="Back-Left">Back-Left</option>
                  <option value="Back-Right">Back-Right</option>
                  <option value="SpareWheel"> Spare Wheel</option>
                </select>
              </div>
              <div class="flex flex-col space-y-1">
                <label class="mt-2" :for="'RTD'+index">Remaining Tread Depth</label>
                <input v-model="tyreData.depth" class="w-[338px] h-[52px] rounded-sm border-solid border border-black" type="text" :id="'RTD'+index" @change="updateTyreData(index)">
              </div>
              <div class="flex flex-col space-y-1">
                <label class="mt-2" :for="'TP'+index">Tyre Pressure (psi)</label>
                <input v-model="tyreData.pressure" class="w-[338px] h-[52px] rounded-sm border-solid border border-black" type="text" :id="'TP'+index" @change="updateTyreData(index)">
              </div>
              <div class="flex flex-col space-y-1">
                <label class="mt-2" :for="'COM'+index">Comment</label>
                <input v-model="tyreData.comment" class="w-[338px] h-[52px] rounded-sm border-solid border border-black" type="text" :id="'COM'+index" @change="updateTyreData(index)">
              </div>
              <div> 
                <FeatherIcon name="trash-2" class="mt-11 w-8 h-8 cursor-pointer text-red-500" @click="deleteTyre(index)" />
              </div>
            </div>
            <div class="flex flex-row space-x-20">
              <div class="flex flex-row items-center space-x-3 ml-4">
                <input v-model="tyreData.wear" class="rounded-sm border border-black bg-gray-200" type="checkbox" id="IW">
                <label for="IW">Irregular Wear</label>
              </div>
              <div class="flex flex-row items-center space-x-3">
                <input v-model="tyreData.cut" class="rounded-sm border border-black bg-gray-200" type="checkbox" id="C/D">
                <label for="C/D">Cut/Damage</label>
              </div>
              <div class="flex flex-row items-center space-x-3">
                <input v-model="tyreData.mark" class="rounded-sm border border-black bg-gray-200" type="checkbox" id="RFM">
                <label for="RFM">Run Flat MARK</label>
              </div>
              <div class="flex flex-row items-center space-x-3">
                <input v-model="tyreData.damage" class="rounded-sm border border-black bg-gray-200" type="checkbox" id="DM">
                <label for="DM">Damage</label>
              </div>
              <div class="flex flex-row items-center space-x-3">
                <input v-model="tyreData.bulge" class="rounded-sm border border-black bg-gray-200" type="checkbox" id="BL">
                <label for="BL">Bulge</label>
              </div>                        
              <div class="flex flex-row items-center space-x-3">
                <input v-model="tyreData.puncture" class="rounded-sm border border-black bg-gray-200" type="checkbox" id="PUN">
                <label for="PUN">Puncture</label>
              </div>  
            </div>
          </div>
        </div>
      </div>
      <!-- Required Services -->
      <div v-if="currentstep==2"> 
        <div class="pt-24"> 
          <h1 class="text-[20px] font-bold mb-1">Required Services</h1>
          <hr class="mt-2" :style="{ borderWidth: '2px', borderColor: 'gray' }">
          <div class="mt-6 flex flex-row space-x-[250px] p-7 bg-gray-200 rounded-lg shadow-md transition-shadow duration-300 hover:shadow-lg"> 
            <!-- col-1 -->
            <div class="flex flex-col space-y-4 mt-4"> 
              <div class="flex flex-row items-center space-x-3"> 
                <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox" id="alignment" @change="handleShow('alignment')">
                <label class="text-[18px]" for="alignment">Alignment</label>
              </div>
              <div class="flex flex-row items-center space-x-3">
                <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox" id="rotation" @change="handleShow('rotation')">
                <label class="text-[18px]" for="rotation">Rotation</label>
              </div>
              <div class="flex flex-row items-center space-x-3">
                <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox" id="oil_change" @change="handleShow('oil_change')">
                <label class="text-[18px]" for="oil_change">Oil Change</label>
              </div>  
              <div class="flex flex-row items-center space-x-3">
                <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox" id="balancing" @change="handleShow('balancing')">
                <label class="text-[18px]" for="balancing">Balancing</label>
              </div>  
              <div class="flex flex-row items-center space-x-3">
                <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox" id="inflation" @change="handleShow('inflation')">
                <label class="text-[18px]" for="inflation">Inflation</label>
              </div>    
            </div>            
            <!-- col-2 -->
            <div class="flex flex-col space-y-4 mt-4"> 
              <div class="flex flex-row items-center space-x-3"> 
                <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox" id="puncture" v-model="services[5].puncture_details" @change="updateData()">
                <label class="text-[18px]" for="puncture">Puncture</label>
              </div>
              <div class="flex flex-row items-center space-x-3">
                <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox" id="tyre_edge" v-model="services[6].tyre_edge_details" @change="updateData()">
                <label class="text-[18px]" for="tyre_edge">Tyre Edge</label>
              </div>
              <div class="flex flex-row items-center space-x-3">
                <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox" id="tyre_batch" v-model="services[7].tyre_batch_details" @change="updateData()">
                <label class="text-[18px]" for="tyre_batch">Tyre Batch</label>
              </div>  
              <div class="flex flex-row items-center space-x-3">
                <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox" id="mushroom_batch" v-model="services[8].mushroom_batch_details" @change="updateData()">
                <label class="text-[18px]" for="mashroom_batch">Mushroom Batch</label>
              </div>
            </div>
            <!-- col-3 -->
            <div class="flex flex-col space-y-4 mt-4"> 
              <div class="flex flex-row items-center space-x-3"> 
                <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox" id="ac_service" @change="handleShow('ac_service')">
                <label class="text-[18px]" for="ac_service">AC Service</label>&emsp;
                <select v-if="show.Ac" class="w-[338px] h-[52px] rounded-sm" style="border: 1px solid black;" v-model="services[9].ac_service_details.service" @change="updateData()">
                  <option value="" selected disabled hidden>Please select...</option>
                  <option value="good">Good</option>
                  <option value="better">Better</option>
                  <option value="not_good">Not Good</option>
                </select>
              </div>
              <div class="flex flex-row items-center space-x-3">
                <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox" id="battery" @change="handleShow('battery')">
                <label class="text-[18px]" for="battery">Battery</label>&emsp;&emsp;&emsp;
                <select v-if="show.battery" class="w-[338px] h-[52px] rounded-sm" style="border: 1px solid black;" v-model="services[10].battery_details.service" @change="updateData()">
                  <option value="" selected disabled hidden>Please select...</option>
                  <option value="good">Good</option>
                  <option value="better">Better</option>
                  <option value="not_good">Not Good</option>
                </select>
              </div>
              <div class="flex flex-row items-center space-x-3">
                <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox" id="wiper" @change="handleShow('wiper')">
                <label class="text-[18px]" for="wiper">Wiper</label>&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp;
                <select v-if="show.wiper" class="w-[338px] h-[52px] rounded-sm" style="border: 1px solid black;" v-model="services[11].wiber_details.service" @change="updateData()">
                  <option value="" selected disabled hidden>Please select...</option>
                  <option value="good">Good</option>
                  <option value="better">Better</option>
                  <option value="not_good">Not Good</option>
                </select>
              </div>  
              <div class="flex flex-row items-center space-x-3">
                <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox" id="car_wash" @change="handleShow('car_wash')">
                <label class="text-[18px]" for="car_wash">Car Wash</label>&emsp;&emsp;
                <select v-if="show.car_wash" class="w-[338px] h-[52px] rounded-sm" style="border: 1px solid black;" v-model="services[12].car_wash_details.service" @change="updateData()">
                  <option value="" selected disabled hidden>Please select...</option>
                  <option value="good">Good</option>
                  <option value="better">Better</option>
                  <option value="not_good">Not Good</option>
                </select>
              </div>
            </div>                        
          </div>
          <!-- hiden fields -->
          <div class="flex flex-col space-y-6 mt-6 ">
            <div v-if="show.alignment" class="p-6 bg-gray-200 rounded-lg shadow-md transition-shadow duration-300 hover:shadow-lg"> 
              <h1 class="text-[20px] font-bold ml-1 mb-6">Alignment Details</h1>
              <div class="flex flex-row space-x-[130px] ml-[55px]"> 
                <div class="flex flex-col space-y-1"> 
                  <label class="text-[16px]" for="LA">Last Alignment (kms)</label>
                  <input class="w-[338px] h-[52px] rounded-sm border-solid border border-black" type="text" id="LA" v-model="services[0].alignment_details.la" @change="updateData()">
                </div>
                <div class="flex flex-col space-y-1"> 
                  <label class="text-[16px]" for="NA">Next Alignment (kms)</label>
                  <input class="w-[338px] h-[52px] rounded-sm border-solid border border-black" type="text" id="NA" v-model="services[0].alignment_details.na" @change="updateData()">
                </div>
              </div>
            </div>
            <div v-if="show.rotation" class="p-6 bg-gray-200 rounded-lg shadow-md transition-shadow duration-300 hover:shadow-lg"> 
              <h1 class="text-[20px] font-bold ml-1 mb-6">Tyre Rotation Details</h1>
              <div class="flex flex-row space-x-[130px] ml-[55px]"> 
                <div class="flex flex-col space-y-1"> 
                  <label class="text-[16px]" for="rim">Rim</label>
                  <input class="w-[338px] h-[52px] rounded-sm border-solid border border-black" type="text" id="rim" v-model="services[1].rotation_details.rim" @change="updateData()">
                </div>
                <div class="flex flex-col space-y-1"> 
                  <label class="text-[16px]" for="wheel">Wheel</label>
                  <input class="w-[338px] h-[52px] rounded-sm border-solid border border-black" type="text" id="wheel" v-model="services[1].rotation_details.wheel" @change="updateData()">
                </div>
              </div>
            </div>
            <div v-if="show.oil_change" class="p-6 bg-gray-200 rounded-lg shadow-md transition-shadow duration-300 hover:shadow-lg"> 
              <h1 class="text-[20px] font-bold ml-1 mb-6">Oil Service</h1>
              <div class="flex flex-row space-x-[130px] ml-[55px]"> 
                <div class="flex flex-col space-y-1"> 
                  <label class="text-[16px]" for="oil_quality">Oil Quality</label>
                  <div> 
                    <select class="w-[338px] h-[52px] rounded-sm" style="border: 1px solid black;" id="oil_quality" v-model="services[2].oil_details.quality" @change="updateData()">
                      <option value="" selected disabled hidden>Please select...</option>
                      <option value="good">Good</option>
                      <option value="ok">Ok</option>
                      <option value="change">Change</option>
                    </select>
                  </div>
                </div>
                <div class="flex flex-col space-y-1"> 
                  <label class="text-[16px]" for="oil_quantity">Oil Quantity</label>
                  <div> 
                    <select class="w-[338px] h-[52px] rounded-sm" style="border: 1px solid black;" id="oil_quantity" v-model="services[2].oil_details.quantity" @change="updateData()">
                      <option value="" selected disabled hidden>Please select...</option>
                      <option value="max">Max</option>
                      <option value="normal">Normal</option>
                      <option value="min">Min</option>
                    </select>
                  </div>
                </div>
              </div>
            </div>
            <div v-if="show.balancing" class="p-6 bg-gray-200 rounded-lg shadow-md transition-shadow duration-300 hover:shadow-lg"> 
              <h1 class="text-[20px] font-bold ml-1 mb-6">Balancing Details</h1>
              <div class="flex flex-row space-x-[70px] ml-[55px]"> 
                <div class="flex flex-col space-y-1"> 
                  <label class="text-[16px]" for="FL">Front-Left (gm)</label>
                  <input class="w-[250px] h-[52px] rounded-sm border-solid border border-black" type="text" id="FL" v-model="services[3].balancing_details.fl" @change="updateData()">
                </div>
                <div class="flex flex-col space-y-1"> 
                  <label class="text-[16px]" for="FR">Front-Right (gm)</label>
                  <input class="w-[250px] h-[52px] rounded-sm border-solid border border-black" type="text" id="FR" v-model="services[3].balancing_details.fr" @change="updateData()">
                </div>
                <div class="flex flex-col space-y-1"> 
                  <label class="text-[16px]" for="BL">Back-Left (gm)</label>
                  <input class="w-[250px] h-[52px] rounded-sm border-solid border border-black" type="text" id="BL" v-model="services[3].balancing_details.bl" @change="updateData()">
                </div>
                <div class="flex flex-col space-y-1"> 
                  <label class="text-[16px]" for="BR">Back-Right (gm)</label>
                  <input class="w-[250px] h-[52px] rounded-sm border-solid border border-black" type="text" id="BR" v-model="services[3].balancing_details.br" @change="updateData()">
                </div>
                <div class="flex flex-col space-y-1"> 
                  <label class="text-[16px]" for="ST">Spare Tyre (gm)</label>
                  <input class="w-[250px] h-[52px] rounded-sm border-solid border border-black" type="text" id="ST" v-model="services[3].balancing_details.st" @change="updateData()">
                </div>
              </div>
            </div>
            <div v-if="show.inflation" class="p-6 bg-gray-200 rounded-lg shadow-md transition-shadow duration-300 hover:shadow-lg"> 
              <h1 class="text-[20px] font-bold ml-1 mb-6">Inflation Details</h1>
              <div class="flex flex-row space-x-[100px] ml-[55px]"> 
                <div class="flex flex-col space-y-5">
                  <div class="flex flex-row space-x-3 mt-3"> 
                    <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox" id="air" :checked="selectedCheckbox === 'air'" @change="handleCheckboxChange('air')">
                    <label class="text-[18px]" for="air">Air</label>
                  </div>
                  <div class="flex flex-row space-x-3"> 
                    <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox" id="nitrogen" :checked="selectedCheckbox === 'nitrogen'" @change="handleCheckboxChange('nitrogen')">
                    <label class="text-[18px]" for="nitrogen">Nitrogen</label>
                  </div>
                </div>
                <div class="flex flex-row space-x-[100px]"> 
                  <div class="flex flex-col space-y-1"> 
                    <label class="text-[16px]" for="FTS">Front Tyres (psi)</label>
                    <input class="w-[338px] h-[52px] rounded-sm border-solid border border-black" type="text" id="FTS" v-model="services[4].inflation_details.fts" @change="updateData()">
                  </div>
                  <div class="flex flex-col space-y-1"> 
                    <label class="text-[16px]" for="RTS">Rear Tyres (psi)</label>
                    <input class="w-[338px] h-[52px] rounded-sm border-solid border border-black" type="text" id="RTS" v-model="services[4].inflation_details.rts" @change="updateData()">
                  </div>
                </div>
              </div>
            </div>     
          </div> 
        </div>
      </div>
      <!-- Replacement Tyre Details -->
      <div v-if="currentstep ==3"> 
        <div class="pt-24" > 
          <h1 class="text-[20px] font-bold mb-1">Tyre Replacement Details</h1>
          <hr class="mt-2 " :style="{ borderWidth: '2px', borderColor: 'gray' }">
          <div class="pb-5 ">
            <div v-for="(position,index) in tyrePositions" :key="index"
            class="grid grid-cols-5 gap-0 mt-7 pb-5 ml-2 border-b border-gray-900 p-2 bg-gray-200 rounded-lg shadow-md transition-shadow duration-300 hover:shadow-lg">
            <div class="ml-5">
              <p class="text-[20px] font-bold mt-8">{{ position }} Tyre</p>
              <div class="mt-[40px]">
                <label>Load Index</label><br>
                <input class="w-[338px] h-[52px] rounded-sm border-solid border border-black" type="text" v-model="tyres[index].loadIndex" @change="saveData(index)">
              </div>
            </div>
            <div class="ml-[100px]">
              <div>
                <label>Brand</label>
                <input class="w-[338px] h-[52px] rounded-sm border-solid border border-black" type="text" v-model="tyres[index].brand" @change="saveData(index)">
              </div>
              <div class="mt-[20px]">
                <label>Speed Rating</label>
                <input class="w-[338px] h-[52px] rounded-sm border-solid border border-black" type="text" v-model="tyres[index].speedRating" @change="saveData(index)">
              </div>
            </div>
            <div class="ml-[200px]">
              <div>
                <label>Pattern</label>
                <input class="w-[338px] h-[52px] rounded-sm border-solid border border-black" type="text" v-model="tyres[index].pattern" @change="saveData(index)">
              </div>
              <div class="mt-[20px]">
                <label>Size</label>
                <input class="w-[338px] h-[52px] rounded-sm border-solid border border-black" type="text" v-model="tyres[index].size" @change="saveData(index)">
              </div>
            </div>
            <div class="ml-[300px]">
              <div>
                <label>TT/TL</label>
                <input class="w-[338px] h-[52px] rounded-sm border-solid border border-black" type="text" v-model="tyres[index].ttTl" @change="saveData(index)">
              </div>
              <div class="mt-[20px]">
                <label>Item</label>
                <input class="w-[338px] h-[52px] rounded-sm border-solid border border-black" type="text" v-model="tyres[index].item" @change="saveData(index)">
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-if="currentstep == 4">
      <div class="pt-24" > 
        <h1 class="text-[20px] font-bold mt-5 mb-1">Raw Materials</h1>
        <table class="table-auto border border-collapse border-gray-800 w-full">
          <thead>
            <tr>
              <th class="text-[20px] border border-gray-800 px-4 py-2">SI.No</th>
              <th class="text-[20px] border border-gray-800 px-4 py-2">Item Code</th>
              <th class="text-[20px] border border-gray-800 px-4 py-2">Source Warehouse</th>
              <th class="text-[20px] border border-gray-800 px-4 py-2">Cost</th>
              <th class="text-[20px] border border-gray-800 px-4 py-2">Required Quantity</th>
            </tr>
          </thead>
          <tbody class="border border-gray-800 text-center">
            <tr v-for="(data, index) in tableData" :key="index">
              <td class="border border-gray-800 px-4 py-2">{{ index + 1 }}</td>
              <td class="border border-gray-800 px-4 py-2">
                <input type="text" class="w-[338px] h-[52px] rounded-sm border-solid border-0 border-black" v-model="data.itemCode">
              </td>
              <td class="border border-gray-800 px-4 py-2">
                <input type="text" class="w-[338px] h-[52px] rounded-sm border-solid border-0 border-black" v-model="data.sourceWarehouse">
              </td>
              <td class="border border-gray-800 px-4 py-2">
                <input type="text" class="w-[338px] h-[52px] rounded-sm border-solid border-0 border-black" style="outline: none;" v-model="data.cost">
              </td>
              <td class="border border-gray-800 px-4 py-2">
                <input type="text" class="w-[338px] h-[52px] rounded-sm border-solid border-0 border-black" v-model="data.requiredQuantity">
              </td>
              <td class="border border-gray-800 px-4 py-2">
                <button class="bg-red-500 w-[100px]  text-white font-bold 0 text-base p-4 rounded-lg ml-3" @click="removeRow(index)">Delete</button>
                <!-- <FeatherIcon name="trash-2" class="mt-11 w-8 h-8 cursor-pointer text-red-500" @click="removeRow(index)" /> -->
              </td>
            </tr>
          </tbody>
        </table>
        <div class="mb-9">
          <button class="bg-blue-500 w-[100px]  text-white font-bold 0 text-base p-4 rounded-lg mt-4" @click="addNewRow">Add row</button>
        </div>
        <div>
          <div class="mt-5 flex">
            <div>
              <p>Total Cost</p>
              <input type="text" class="w-[338px] h-[52px] rounded-sm border-solid border border-black" v-model="totalCost" readonly>
            </div>
            <div class="ml-auto">
              <p>Total Quantity</p>
              <input type="text" class="w-[338px] h-[52px] rounded-sm border-solid border border-black" v-model="totalQuantity" readonly>
            </div>
          </div>
          <div class="mt-5 flex">
            <div>
              <p>Discount Cost</p>
              <input type="text" class="w-[338px] h-[52px] rounded-sm border-solid border border-black" v-model="discountCost" readonly>
            </div>
            <div class="ml-auto">
              <p>Final Amount</p>
              <input type="text" class="w-[338px] h-[52px] rounded-sm border-solid border border-black" v-model="finalAmount" readonly>
            </div>
          </div>
          <div class="mt-5">
            <p>Total Amount</p>
            <input type="text" class="w-[338px] h-[52px] rounded-sm border-solid border border-black" v-model="totalAmount" readonly>
          </div>
        </div>
      </div>
    </div>
    <div v-if="Auth">
      <div class="flex justify-center space-x-5 pb-5 mt-5">
        <button v-if="currentstep !=0" class="bg-blue-500 w-[50%] text-white font-bold  text-base p-4 rounded-lg" @click="previousPage">Preview
        </button>
        <button v-if="currentstep !=4" class="bg-blue-500 w-[50%] text-white font-bold  text-base p-4 rounded-lg"
          @click="nextPageAndHighlight">Next
        </button>
      </div>
      <div class="bottom-div">
        <div class="m-0 p-6 mb-2">
          <ul class="ml-[130px] flex space-x-[250px] text-center">
            <li type="disc" :class="{ 'active': currentPage === 'details' }" @click="setCurrentPage('details',0)">Details</li>
            <li type="disc" :class="{ 'active': currentPage === '5 Points Checkup' }" @click="setCurrentPage('5 Points Checkup',1)">5 Points Checkup</li>
            <li type="disc" :class="{ 'active': currentPage === 'Required Services' }" @click="setCurrentPage('Required Services',2)">Required Services</li>
            <li type="disc" :class="{ 'active': currentPage === 'Tyre Replacement Details' }" @click="setCurrentPage('Tyre Replacement Details',3)">Tyre Replacement Details</li>
            <li type="disc" :class="{ 'active': currentPage === 'Billing Details' }" @click="setCurrentPage('Billing Details',4)">Billing Details</li>
          </ul>
        </div>
      </div>
    </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, reactive, watch } from 'vue';
  import {FeatherIcon} from 'frappe-ui'
  import axios from 'axios';

  //final post data  1)tyreDatas[],


  const selectImg = ref(true);
  const Auth = ref(true)
  const incorrect =ref(false);
  const currentstep = ref(0);

  const data = reactive({
    selectedImgSrc: '',
    selectedAlt: ''
  });

  const pin1 = ref('');
  const pin2 = ref('');
  const pin3 = ref('');
  const pin4 = ref('');

  function handleImgSelection(event) {
    selectImg.value = true;
    data.selectedImgSrc = event.target.src;
    data.selectedAlt = event.target.alt;
    console.log(data.selectedImgSrc, data.selectedAlt);
  }

  function focusNext(event, nextInput) {
    const target = event.target;
    if (target.value.length === 1) {
      const inputs = target.parentNode.querySelectorAll('input');
      if (nextInput < inputs.length) {
        inputs[nextInput].focus();
      }else{
        submitPin();
      }
    }
  }

  function submitPin() {
    if(pin1 && pin2 && pin3 && pin4){
      const pin = pin1.value + pin2.value + pin3.value + pin4.value;
      if(pin === "1234"){
        Auth.value=true;
      }
      else{
            incorrect.value=true;
            pin1.value = pin2.value = pin3.value = pin4.value = '';
            setTimeout(() => {
              incorrect.value = false;
            }, 3000);
        }
    }
  }
//==========================================================>>> Main Page <<<================================================================================//

const searchQuery = ref('');

// const performSearch = () => {
//   const query = searchQuery.value.trim().toLowerCase();
//   console.log('Performing search with query:', query);
//   const vehicleResults = vehicleDetails.data.value.filter(item => {
//     return item.vehicle_number.toLowerCase().includes(query);
//   });
//   console.log('Vehicle search results:', vehicleResults);
// };

const Search = async () => {
  const data = {
    "license_plate": searchQuery.value // Assuming searchQuery is defined elsewhere in your code
  };

  try {
    if (data.license_plate) {
      const response = await axios.post('http://127.0.0.1:8002/api/method/tyre.api.get_details', data);
      console.log(response.data);
    } else {
      alert("Enter a vehicle number...");
    }
  } catch (error) {
    console.log(error);
  }
};

const currentPage = ref('details');
// const currentstep = ref(0);
const maxStep = 4;

function previousPage() {
  if (currentstep.value > 0) {
    currentstep.value--;
    currentPage.value = getPageName(currentstep.value);
  }
}

function nextPageAndHighlight() {
  if (currentstep.value < maxStep) {
    currentstep.value++;
    currentPage.value = getPageName(currentstep.value);
  }
}

function getPageName(step) {
  switch (step) {
    case 0:
      return 'details';
    case 1:
      return '5 Points Checkup';
    case 2:
      return 'Required Services';
    case 3:
      return 'Tyre Replacement Details';
    case 4:
      return 'Billing Details';
    default:
      return 'details';
  }
}

const setCurrentPage = (page,step) => {
  currentPage.value = page;
  currentstep.value = step;
}
const vehicleDetails = ref({
  vehicleNumber: 'TN 47 SL 7784',
  vehicleBrand: 'Tata',
  vehicleModel: 'Indica Vista',
  chassisNo: 3456789,
  fuelType: "Diesel",
  odometerValue: 'Indica Vista',
  tyreChange: '25,000 kms',
  alignment: '10,000 kms'
})

const employeesDetails = ref({
  ownerName: 'Vijayaragavan',
  ownerMobile: 6383436185,
  employees: [
    {
      name: 'siva',
      type: 'Driver',
      contactPerson: 'prakash',
      phone: 9876543210
    },
    {
      name: 'kumar',
      type: 'Customer',
      contactPerson: 'yasin',
      phone: 63741234567
    }
  ]
})

const showNewVehicle = ref(false);
const showNewCustomer = ref(false)
const showModifyVehicle = ref(false);
const showModifyCustomer = ref(false);

const addVehicle = () => {
  showNewVehicle.value = !showNewVehicle.value;
};
const addCustomer = () => {
  showNewCustomer.value = !showNewCustomer.value;
}
const modifyVehicle = () => {
  showModifyVehicle.value = !showModifyVehicle.value;
}
const modifyCustomer = () => {
  showModifyCustomer.value = !showModifyCustomer.value;
}
const employees = ref([{ name: '', type: '', phone: '' }]);
function moreEmployee() {
  employees.value.push({ name: '', type: '', phone: '' });
}

function modifiedMoreEmployee() {
  employeesDetails.value.employees.push({
    name: '',
    type: ''
  });
}
const vehicleData = ref({
  vehicleNumber: '',
  vehicleBrand: '',
  vehicleModel: '',
  chassisNo: '',
  fuelType: '',
  odometerValue: '',
  tyreChange: '',
  alignment: ''
});
const addVehicleData = () => {
  const fieldNames = Object.keys(vehicleData.value);
  const data = {};

  fieldNames.forEach(fieldName => {
    const value = vehicleData.value[fieldName].trim();
    if (value == '') {
      return
    }
    data[fieldName] = value;
    vehicleData.value[fieldName] = '';
  });
  console.log(data);
};

const addModifiedData = () => {
  console.log('saved', vehicleDetails.value);
}

const addModifiedCustomerData = () => {
  const ownerName = employeesDetails.value.ownerName;
  const ownerMobile = employeesDetails.value.ownerMobile;
  const employees = employeesDetails.value.employees;
  const data = {
    ownerName: ownerName,
    ownerMobile: ownerMobile,
    employees: []
  };

  employees.forEach((employee, index) => {
    const name = employee.name.trim();
    if (name === '') {
      return;
    }
    data.employees.push({
      name: name,
      type: employee.type,
      contactperson: employee.contactPerson,
      phone: employee.phone
    });
  });
  console.log(data);
};

const removeModifiedCustomerData = () => {
  employeesDetails.value.ownerName = '';
  employeesDetails.value.ownerMobile = '';
  employeesDetails.value.employees = [];
}

const clearModifiedVehicleData = () => {
  Object.keys(vehicleDetails.value).forEach(key => {
    vehicleDetails.value[key] = '';
  });
}

const clearVehicleData = () => {
  Object.keys(vehicleData.value).forEach(key => {
    vehicleData.value[key] = '';
  });
};

const customerData = ref({
  ownerName: '',
  ownerMobile: '',
  employees: employees.value,
});

const addCustomerData = () => {
  const ownerName = customerData.value.ownerName.trim();
  const ownerMobile = customerData.value.ownerMobile.trim();
  if (!ownerName && !ownerMobile) {
    alert("Please fill in at least one of the fields: Owner Name or Owner Mobile");
    return;
  }
  if (employees.value.length === 0) {
    alert("Please add at least one employee");
    return;
  }
  const isAnyEmployeeDataMissing = employees.value.some(employee => {
    return !employee.name.trim() || !employee.type.trim();
  });
  if (isAnyEmployeeDataMissing) {
    alert("Please fill in all fields for all employees");
    return;
  }
  const data = {
    ownerName: customerData.value.ownerName,
    ownerMobile: customerData.value.ownerMobile,
    employees: []
  };

  employees.value.forEach(employee => {
    data.employees.push({
      name: employee.name,
      type: employee.type
    });
  });

  Object.keys(customerData.value).forEach(key => {
    customerData.value[key] = '';
  });
  employees.value = [{ name: '', type: '' }];

  console.log("Owner name:", data.ownerName);
  console.log("Owner mobile:", data.ownerMobile);

  data.employees.forEach(employee => {
    console.log("Employee Name:", employee.name);
    console.log("Employee Type:", employee.type);
  });

  console.log(data);
};

const removeCustomerData = () => {
  Object.keys(customerData.value).forEach(key => {
    customerData.value[key] = '';
  });
  employees.value = [{ name: '', type: '' }];
}

const removeEmployee2 = (index) => {
  employeesDetails.value.employees.splice(index, 1);
};
const removeEmployee1 = (index) => {
  employees.value.splice(index, 1);
};


//==========================================================>>> 5 point checkup <<<==========================================================================//

  const tyreDatas = ref([{ tyre: '', depth: '', pressure: '', comment: '', wear: false, cut: false, mark: false, damage: false, bulge: false, puncture: false }]);

const addTyre = () => {
    tyreDatas.value.push({ tyre: '', depth: '', pressure: '', comment: '', wear: false, cut: false, mark: false, damage: false, bulge: false, puncture: false });
};

const updateTyreData = (index) => {
    const tyre = tyreDatas.value[index];
    console.log('Updated tyre data:', tyre);
    console.log(tyreDatas.value);
};

const deleteTyre = (index) => {
    tyreDatas.value.splice(index, 1);
};

//========================================================>>> Required Services <<<============================================================================//

const selectedCheckbox =ref('');
const services = ref([
    // (0)
    { name: 'Alignment', alignment_details: {la: '',na: ''}},
    // (1)
    { name: 'Rotation',rotation_details: {rim: '',wheel: ''}},
    // (2)
    { name: 'Oil Change',oil_details: {quality: '',quantity: ''}},
    // (3)
    { name: 'Balancing',balancing_details: {fl: '',fr: '',bl: '',br: '',st: ''}},
    // (4)
    { name: 'Inflation',inflation_details: {air_type:'',fts: '',rts: ''}},
    // (5)
    { name: 'Puncture', puncture_details: false},
    // (6)
    { name: 'Tyre Edge', tyre_edge_details: false},
    // (7)
    { name: 'Tyre Batch', tyre_batch_details: false},
    // (8)
    { name: 'Mushroom Batch',mushroom_batch_details: false},
    // (9)
    { name: 'AC Service',ac_service_details: {service: ''}},
    // (10)
    { name: 'Battery',battery_details: {service: ''}},
    // (11)
    { name: 'Wiper', wiber_details: {service: ''}},
    // (12)
    { name: 'Car Wash',car_wash_details: {service: ''}}
  ]);

const show=ref({
    alignment:false,//store in two data in la,na value
    rotation:false,//store in two data in rim,wheel value
    oil_change:false,//store in two data quality,quantity
    balancing:false,//store in five data fl,fr,bl,br,st
    inflation:false,//store in three value (air,nitrogen),fts,rts
    puncture:false,
    type_edge:false,
    tyre_batch:false,
    mushroom_batch:false,
    Ac:false,//its store selection data single input
    battery:false,//its store selection data single input
    wiper:false,//its store selection data single input
    car_wash:false,//its store selection data single input
})

function handleCheckboxChange(checkboxId) {
      if (this.selectedCheckbox === checkboxId) {
        selectedCheckbox = null;
      } else {
        selectedCheckbox.value = checkboxId;
        // console.log(selectedCheckbox.value)
        services.value[4].inflation_details.air_type=selectedCheckbox.value;
        console.log(services.value[4].inflation_details.air_type);
        const otherCheckboxId =checkboxId === 'air' ? 'nitrogen' : 'air';
        const otherCheckbox = document.getElementById(otherCheckboxId);
        if (otherCheckbox) {
          otherCheckbox.checked = false;
        }
      }
    }
    function handleShow(item){
    switch(item) {
        case 'ac_service':
            show.value.Ac = !show.value.Ac;
            break;
        case 'battery':
            show.value.battery = !show.value.battery;
            break;
        case 'wiper':
            show.value.wiper = !show.value.wiper;
            break;
        case 'car_wash':
            show.value.car_wash = !show.value.car_wash;
            break;
        case 'alignment':
            show.value.alignment = !show.value.alignment;
            break;
        case 'rotation':
            show.value.rotation = !show.value.rotation;
            break; 
        case 'oil_change':
            show.value.oil_change = !show.value.oil_change;
            break; 
        case 'balancing':
            show.value.balancing = !show.value.balancing;
            break; 
        case 'inflation':
            show.value.inflation = !show.value.inflation;
            break;                 
    }
}

  function updateData(){
    console.log(services);
  }

//===================================================>>> Replacement Tyre Details <<<========================================================================//

const tyrePositions = ['Front Left', 'Front Right', 'Rear Left', 'Rear Right', 'Spare'];
  
  const tyres = ref(Array.from({ length: tyrePositions.length }, () => ({
    loadIndex: '',
    brand: '',
    speedRating: '',
    pattern: '',
    size: '',
    ttTl: '',
    item: ''
  })));
  
  const saveData = (index) => {
    console.log(tyres.value);
  };

//===================================================>>>Last Page <<<=========================================================================================//

const tableData = ref([]);
const totalCost = ref(0);
const totalQuantity = ref(0);
const discountCost = ref(0);
const finalAmount = ref(0);
const totalAmount = ref(0);

const calculateTotals = () => {
  totalCost.value = 0;
  totalQuantity.value = 0;
  totalAmount.value = 0;

  tableData.value.forEach(row => {
    totalCost.value += parseFloat(row.cost) || 0;
    totalQuantity.value += parseFloat(row.requiredQuantity) || 0;
  });

  const discountRate = calculateDiscountRate(totalQuantity.value);
  discountCost.value = totalCost.value * discountRate;

  finalAmount.value = totalCost.value - discountCost.value;
  totalAmount.value = totalQuantity.value * finalAmount.value
};

const calculateDiscountRate = (quantity) => {
  if (quantity >= 100) {
    return 0.1;
  } else if (quantity >= 50) {
    return 0.05;
  } else {
    return 0.01;
  }
};

watch(tableData, () => {
  calculateTotals();
}, { deep: true });

const addNewRow = () => {
  tableData.value.push({
    sno: '',
    itemCode: '',
    cost: '',
    sourceWarehouse: '',
    requiredQuantity: ''
  });
};

const removeRow = (index) => {
  tableData.value.splice(index, 1);
};

</script>

<style scoped>
/* Add your CSS styles here */
.dark-hr {
  height: 2px;
  background-color: #000000 !important;
}

p {
  font-size: 20px;
}

.bottom-div {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: #f0f0f0;
}

.active {
  font-weight: bold;
}
</style>
