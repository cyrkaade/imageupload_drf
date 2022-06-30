# there are my 60% tries and unworked code

  # def save(self, *args, **kwargs):
    #     super(User, self).save(*args, **kwargs)
    #     if User.is_premium:
    #         if not User.is_enterprise:
    #             User.is_basic = None
    #             User.is_premium = True
    #             User.is_enterprise = None
    #             super(User, self).save(*args, **kwargs)
    #     elif User.is_premium:
    #         if User.is_enterprise:
    #             User.is_premium = None
    #             User.is_basic = None
    #             User.is_enterprise = True
    #             super(User, self).save(*args, **kwargs)
    #     else:
    #         User.is_premium = None
    #         User.is_basic = True
    #         User.is_enterprise = None
    #         super(User, self).save(*args, **kwargs)

    # original = models.ImageField('Original image', default='uploaded_media/PNG_transparency_demonstration_1.png')
    # # small = ResizedImageField(size=[200, 200], blank=True, null=True)
    # # medium = ResizedImageField(size=[400, 400], blank=True, null=True)
    # small = ImageSpecField(
    #     source='original', processors=[ResizeToFill(200, 200)], format='JPEG', options={'quality': 60})
    # medium = ImageSpecField(
    #     source='original', processors=[ResizeToFill(400, 400)], format='JPEG', options={'quality': 60})
    # def save(self, *args, **kwargs):

    #     super(UploadImage, self).save(*args, **kwargs)

# str_original = str(self.original)
            # img=cv2.imread(str_original)

# self.expiring_image_url.delete()
                # async_timer = sync_to_async(timeer(int(self.expire_secs_only_for_enterprise)), thread_sensitive=False)
                # async_deleting = sync_to_async(delete_expiring(self.expiring_image_url), thread_sensitive=True)
                # async_timer()
                # async_deleting()
                # expire_secs = models.PositiveIntegerField(MaxValueValidator=300, MinValueValidator=3000)
                # pk = req.pk
                # # await updating(self, req, self.expiring_image_url, self.original, secs=expire_secs, pk=pk)
                # super(UploadImage, self).save()

# def my_view(request):
#     username = None
#     if request.user.is_authenticated():
#         username = request.user.username
#     return username

# @api_view(["DELETE"])
# def product_delete_rest_endpoint(request, pk):
#     UploadImage.objects.get(pk=pk).delete()
#     return Response()
        
# def put(self, request, *args, **kwargs):
#     pk = request.query_params["pk"]
#     image_object = UploadImage.objects.get(pk=pk)

#     data = request.data

#     image_object.original = data["original"]
#     image_object.small = data["small"]
#     image_object.medium = data["medium"]
#     image_object.expiring_image_url = data["expiring_image_url"]
#     image_object.engine_type = data["engine_type"]

#     image_object.save()

#     serializer = UploadImageSerializer(image_object)
#     return Response(serializer.data)

# @sync_to_async
# def async_view(request):
#   loop = asyncio.get_event_loop()
#   loop.create_task(updating())

# class UploadImageView(APIView):

#     parser_classes = (MultiPartParser, FormParser, )

#     def post(self, request, format=None):
#         uploaded_file = request.FILES['image']
#         print('up_file is',uploaded_file)
#         filename = 'uploaded_media/'
#         with open(filename, 'wb+') as destination:
#             for chunk in uploaded_file.chunks():
#                 print('chunk',chunk)
#                 destination.write(chunk)
#                 destination.close()

#         my_saved_file = open(filename)
#         return Response(uploaded_file.name, status.HTTP_201_CREATED)


# generates the string of the one time URL
# def randomString(stringLength=20):
#     """Generate a random string of fixed length """
#     letters = string.ascii_lowercase
#     return ''.join(random.choice(letters) for i in range(stringLength))

# generates the link itself
# def generate_link(request):
#     the_string = randomString(stringLength=20)
#     UploadImage.objects.create(one_time_code=the_string)
#     return HttpResponse('<a href="/polls/one_time_link/{}">{}{}</a>'.format(the_string, request.build_absolute_uri(), the_string))


#handles the link request
# def one_time_link(request,access_code=0):

#     if (access_code == 0):
#         return HttpResponse("Test link")

#     elif UploadImage.objects.filter(one_time_code=access_code).exists() and datetime.now > datetime.now:

#         #remove the line below if you do not want the link to self destruct after it has been used
#         UploadImage.objects.filter(one_time_code=access_code).delete()
#         return HttpResponse("Hey, your linked worked. Make sure to download as it won't work again.")

#     elif not UploadImage.objects.filter(one_time_code=access_code).exists():
#         return HttpResponse("Bad or expired link.")
#     else:
#         return HttpResponse("Bad or expired link.")

# class FileUploadView(APIView):
#     parser_classes = (FileUploadParser, )

#     def post(self, request, format=None):
#         uploaded_file = request.FILES['file']
#         print('up_file is',uploaded_file)
#         with open('/media/'+uploaded_file.name, 'wb+') as destination:
#             for chunk in uploaded_file.chunks():
#                 print('chunk',chunk)
#                 destination.write(chunk)
#                 destination.close()
#         return Response(uploaded_file.name, status.HTTP_201_CREATED)

# class RentalList(generics.ListCreateAPIView):
#     serializer_class = UploadImageSerializer
#     queryset = UploadImage.objects.all()
#     def get(self,request,format=None):
#         rental = self.get_queryset()
#         serializer_rental = UploadImageSerializer(rental,many=True)
#         return Response(serializer_rental.data)

#     # @permission_classes((IsAdminUser, ))
#     # def post(self,request,format=None):
#     #     user=request.user
#     #     serializer_rental = UploadImageSerializer(data=request.data,context={'user':user})
#     #     if serializer_rental.is_valid():
#     #         serializer_rental.save()
#     #         return Response(serializer_rental.data,status=status.HTTP_201_CREATED)
#     #     return Response(serializer_rental.errors,status=status.HTTP_400_BAD_REQUEST)


# class RentalDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset=UploadImage.objects.all()
#     serializer_class = UploadImageSerializer

# def updating(self, request, module, expiring_image_url, original, secs):
#     random_str = token_hex(16)
#     make_copy(expiring_image_url, original, f'{random_str}')
#     super(module, self).save()
#     time.sleep(int(secs))
#     module.expiring_image_url.delete(save=True)